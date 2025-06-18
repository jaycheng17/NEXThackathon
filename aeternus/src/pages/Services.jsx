import { useAuth } from "react-oidc-context";
import "../css/Services.css";

function Services() {
  const auth = useAuth();

  const signOutRedirect = () => {
    const clientId = "2edgpr2d91i7rds9hejqif6nkp";
    const logoutUri = "http://localhost:5173/";
    const cognitoDomain = "https://us-west-24rvtrtb91.auth.us-west-2.amazoncognito.com";
    window.location.href = `${cognitoDomain}/logout?client_id=${clientId}&logout_uri=${encodeURIComponent(logoutUri)}`;
  };

  const fetchData = async (event) => {
    event.preventDefault(); // Prevent the default form submission behavior
    const formData = {
      url: document.getElementById("url").value
    };

    const result = await fetch("https://w5l55ytt15.execute-api.us-west-2.amazonaws.com/dev/test2", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(formData)
    });

    if (result.ok) {
      const data = await result.json();
      const bodyData = JSON.parse(data.body)
      console.log(bodyData)

      const inputDiv = document.getElementById("inputDiv");
      const servicesDiv = document.getElementById("servicesDiv");
      servicesDiv.removeChild(inputDiv)

      const promptDiv = document.createElement("div");
      promptDiv.classList.add("promptDiv");
      promptDiv.textContent = `Prompt: ${bodyData}`;
      promptDiv.style.display = "block";
      servicesDiv.appendChild(promptDiv);
    }

  }

  if (auth.isLoading) {
    return (<div className="loader-container">
      <span className="loader"></span>
    </div>);
  }

  if (auth.error) {
    return (
      <div className="errordiv">
        <p>Error: {auth.error.message}</p>
        <button className="signbtn" onClick={() => auth.signinRedirect()}>Retry Sign in</button>
      </div>
    );
  }

  if (2==2) {
    return (
      <div id='servicesDiv'>
        <div id="inputDiv">
          <form>
            Enter Your Pinterest Board Link:
            <input type="text" name="pinterest_board_url" id="url" />
            <button onClick={fetchData} id="submitBtn">Submit</button>
          </form>
        </div>


        <div className="logoutdiv">
          <button className="signbtn" onClick={() => { auth.removeUser(); signOutRedirect(); }}>Sign out</button>
        </div>
      </div>
    );
  }

  return (
    <div className="logindiv">
      <button className="signbtn" onClick={() => auth.signinRedirect()}>Sign in</button>
    </div>
  );
}

export default Services;