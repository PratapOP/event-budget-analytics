const ctx = document.getElementById("budgetChart");

new Chart(ctx, {
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
                "rgba(56, 189, 248, 0.7)",
                "rgba(248, 113, 113, 0.7)",
                "rgba(74, 222, 128, 0.7)"
            ],
            borderRadius: 8
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                labels: {
                    color: "#e2e8f0"
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: "#cbd5e1"
                },
                grid: {
                    color: "rgba(255,255,255,0.05)"
                }
            },
            y: {
                ticks: {
                    color: "#cbd5e1"
                },
                grid: {
                    color: "rgba(255,255,255,0.05)"
                }
            }
        }
    }
});