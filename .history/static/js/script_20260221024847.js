async function predictBudget() {

    const planned = document.getElementById("planned").value;
    const actual = document.getElementById("actual").value;
    const sponsorship = document.getElementById("sponsorship").value;

    // Basic validation
    if (!planned || !actual || !sponsorship) {
        document.getElementById("result").innerText =
            "Please fill all fields.";
        document.getElementById("result").style.color = "#f87171";
        return;
    }

    // Send data to Flask backend
    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            planned: planned,
            actual: actual,
            sponsorship: sponsorship
        })
    });

    const data = await response.json();

    // Display result with styling
    if (data.over_budget === 1) {
        document.getElementById("result").innerText =
            "⚠️ High Risk: Event likely over budget";
        document.getElementById("result").style.color = "#f87171";
    } else {
        document.getElementById("result").innerText =
            "✔️ Safe: Budget looks under control";
        document.getElementById("result").style.color = "#4ade80";
    }
}