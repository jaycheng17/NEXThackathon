import "../css/Services.css";

function Services() {


  const fetchData = async (event) => {
    event.preventDefault(); // Prevent the default form submission behavior
    const formData = {
      url: document.getElementById("url").value
    };

    const result = await fetch("https://w5l55ytt15.execute-api.us-west-2.amazonaws.com/default/test2", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(formData)
    });

    if (result.ok) {
      const data = await result.json();
      const bodyData = JSON.parse(data.body)


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
  return (
    <div id='servicesDiv'>
      <div id="inputDiv">
        <form>
          Enter Your Pinterest Board Link:
          <input type="text" name="pinterest_board_url" id="url" />
          <button onClick={fetchData} id="submitBtn">Submit</button>
        </form>
      </div>
    </div>

  );

}


export default Services;