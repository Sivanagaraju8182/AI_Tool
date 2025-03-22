async function sendRequest() {
    const userInput = document.getElementById("userInput").value.trim();
    if (!userInput) {
        alert("Please enter a question!");
        return;
    }

    document.getElementById("userQuestion").innerText = userInput;
    document.getElementById("aiResponse").innerText = "Thinking... 🤔";

    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ prompt: userInput })
        });

        if (!response.ok) {
            throw new Error("Network response was not ok");
        }

        const data = await response.json();
        document.getElementById("aiResponse").innerText = data.response;
    } catch (error) {
        document.getElementById("aiResponse").innerText = "⚠️ Error: AI is not responding!";
        console.error("Fetch error:", error);
    }
}
