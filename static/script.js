document.getElementById("summarizeBtn").addEventListener("click", async function() {
    const text = document.getElementById("inputText").value;
    const numSentences = document.getElementById("numSentences").value;

    if (text.trim() === "") {
        alert("Please enter some text to summarize.");
        return;
    }

    try {
        const response = await fetch("/summarize", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text, numSentences: numSentences })
        });

        const result = await response.json();
        document.getElementById("summaryOutput").innerText = result.summary;
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred while summarizing the text.");
    }
});
