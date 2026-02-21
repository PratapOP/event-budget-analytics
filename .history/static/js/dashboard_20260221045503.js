// ===============================
// BUDGET VS ACTUAL BAR CHART
// ===============================
const budgetCtx = document.getElementById("budgetChart");

new Chart(budgetCtx, {
    type: "bar",
    data: {
        labels: ["Planned Budget", "Actual Spend", "Sponsorship"],
        datasets: [{
            label: "Amount",
            data: [
                parseFloat(document.querySelectorAll(".kpi-value")[0].innerText.replace("₹","")),
                parseFloat(document.querySelectorAll(".kpi-value")[1].innerText.replace("₹","")),
                parseFloat(document.querySelectorAll(".kpi-value")[2].innerText.replace("₹",""))
            ],
            backgroundColor: [
                "rgba(56,189,248,0.7)",
                "rgba(248,113,113,0.7)",
                "rgba(74,222,128,0.7)"
            ],
            borderRadius: 8
        }]
    },
    options: {
        plugins: {
            legend: {
                labels: { color: "#e2e8f0" }
            }
        },
        scales: {
            x: { ticks: { color: "#cbd5e1" } },
            y: { ticks: { color: "#cbd5e1" } }
        }
    }
});


// ===============================
// CATEGORY PIE CHART
// ===============================
const categoryCtx = document.getElementById("categoryChart");

new Chart(categoryCtx, {
    type: "pie",
    data: {
        labels: categoryLabels,
        datasets: [{
            data: categoryValues,
            backgroundColor: [
                "#38bdf8",
                "#f87171",
                "#4ade80",
                "#fbbf24",
                "#a78bfa",
                "#fb7185"
            ]
        }]
    },
    options: {
        plugins: {
            legend: {
                labels: { color: "#e2e8f0" }
            }
        }
    }
});


// ===============================
// MONTHLY TREND LINE CHART
// ===============================
const trendCtx = document.getElementById("trendChart");

new Chart(trendCtx, {
    type: "line",
    data: {
        labels: monthLabels,
        datasets: [{
            label: "Monthly Spend",
            data: monthValues,
            borderColor: "#38bdf8",
            backgroundColor: "rgba(56,189,248,0.2)",
            fill: true,
            tension: 0.3
        }]
    },
    options: {
        plugins: {
            legend: {
                labels: { color: "#e2e8f0" }
            }
        },
        scales: {
            x: { ticks: { color: "#cbd5e1" } },
            y: { ticks: { color: "#cbd5e1" } }
        }
    }
});