import "../css/Services.css";

function Services() {


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

  if (auth.isAuthenticated) {
    return (
      <div>
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

  const fetchData = async (event) => {
    event.preventDefault(); // Prevent the default form submission behavior
    const formData = {
      url: document.getElementById("url").value
    };

    const result = await fetch("https://dz7ljnan0l.execute-api.us-west-2.amazonaws.com/TestAPI", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(formData)
    });

    if (result.ok) {
      const data = await result.json();
      console.log(data);
      // document.getElementById("inputDiv").style.display = "none";
      // document.getElementById("promptDiv").textContent = `${data}`;
      // document.getElementById("promptDiv").classList.add("promptDiv");
    }
  }

  return (
    <div className="logindiv">
      <button className="signbtn" onClick={() => auth.signinRedirect()}>Login / Signup</button>
    </div>
  );
}

export default Services;