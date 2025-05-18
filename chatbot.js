function sendMessage(userMessage) {
  fetch("http://localhost:5000/process?message=" + encodeURIComponent(userMessage))
    .then(response => {
      if (!response.ok) {
        throw new Error("Server responded with status " + response.status);
      }
      return response.json();
    })
    .then(data => {
      console.log("Wit.ai response:", data);
      // display data in the chat UI
    })
    .catch(error => {
      console.error("Error contacting the server:", error);
      alert("There was an error contacting the server. Try again.");
    });
}
