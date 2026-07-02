document.addEventListener("DOMContentLoaded", function () {

    // Search Tables
    const searchBoxes = document.querySelectorAll(
        "#searchInput,#storageSearch"
    );

    searchBoxes.forEach(searchBox => {

        if (!searchBox) return;

        searchBox.addEventListener("keyup", function () {

            const value =
                this.value.toLowerCase();

            const tables =
                document.querySelectorAll("tbody tr");

            tables.forEach(row => {

                const text =
                    row.textContent.toLowerCase();

                row.style.display =
                    text.includes(value)
                        ? ""
                        : "none";

            });

        });

    });

    // Status Filter
    const statusFilter =
        document.getElementById("statusFilter");

    if (statusFilter) {

        statusFilter.addEventListener("change", function () {

            const selected =
                this.value;

            const rows =
                document.querySelectorAll(
                    "#claimTable tbody tr"
                );

            rows.forEach(row => {

                const status =
                    row.cells[5].textContent.trim();

                if (
                    selected === "all" ||
                    status === selected
                ) {
                    row.style.display = "";
                } else {
                    row.style.display = "none";
                }

            });

        });

    }

});

// Claim Submission
const claimForm =
    document.getElementById("claimForm");

if (claimForm) {

    claimForm.addEventListener("submit", function (e) {

        e.preventDefault();

        const claimId =
            document.getElementById("claimId").value;

        const patient =
            document.getElementById("patientName").value;

        const hospital =
            document.getElementById("hospital").value;

        const department =
            document.getElementById("department").value;

        const amount =
            document.getElementById("amount").value;

        if (
            claimId === "" ||
            patient === "" ||
            hospital === "" ||
            department === "" ||
            amount === ""
        ) {

            alert("Please fill all fields");
            return;
        }

        alert("Claim Submitted Successfully");

        claimForm.reset();

    });

}

// Download Report
function downloadReport() {

    const content =
        "Healthcare Claims Report Generated Successfully";

    const blob =
        new Blob([content],
            { type: "text/plain" });

    const link =
        document.createElement("a");

    link.href =
        URL.createObjectURL(blob);

    link.download =
        "Claims_Report.txt";

    link.click();

}

// Export CSV
function exportCSV() {

    let csv =
`ClaimID,Patient,Hospital,Status
CL001,Rahul Patil,City Care Hospital,Approved
CL002,Priya Sharma,Lifeline Hospital,Pending
CL003,Amit Verma,Sunshine Hospital,Rejected`;

    let blob =
        new Blob([csv],
            { type: "text/csv" });

    let link =
        document.createElement("a");

    link.href =
        URL.createObjectURL(blob);

    link.download =
        "claims_data.csv";

    link.click();

}

// Database Backup
function backupDatabase() {

    alert(
        "Database Backup Completed Successfully"
    );

}

// Download PDF Demo
function downloadPDF() {

    const content =
`Healthcare Claims Analytics Portal

Claim Report

Claim ID : CL009
Patient : Vikram Shah
Status : Approved
Amount : ₹2,20,000`;

    const blob =
        new Blob([content],
            { type: "application/pdf" });

    const link =
        document.createElement("a");

    link.href =
        URL.createObjectURL(blob);

    link.download =
        "Claim_Report.pdf";

    link.click();

}

// Print
function printReport() {

    window.print();

}

// Notifications
function showNotification(message) {

    let note =
        document.createElement("div");

    note.innerHTML =
        message;

    note.style.position = "fixed";
    note.style.top = "20px";
    note.style.right = "20px";
    note.style.background = "#10b981";
    note.style.color = "#fff";
    note.style.padding = "15px";
    note.style.borderRadius = "10px";
    note.style.zIndex = "9999";

    document.body.appendChild(note);

    setTimeout(() => {
        note.remove();
    }, 3000);

}



function submitClaim(){

document.getElementById("successMsg").style.display = "block";

}

function downloadReport(){

const report = `
Healthcare Claims Analytics Portal

Claim ID : CL031
Patient Name : Rahul Patil
Hospital : City Care Hospital
Department : Cardiology
Amount : ₹85,000
Status : Approved
`;

const blob = new Blob([report], {type:"text/plain"});

const link = document.createElement("a");

link.href = URL.createObjectURL(blob);

link.download = "Claim_Report_CL031.txt";

link.click();

}

function createBackup(){

document.getElementById("backupMsg").style.display="block";

const backupData =
`Database Backup
Claim ID : CL031
Patient : Rahul Patil
Status : Approved`;

const blob = new Blob([backupData], {type:"text/plain"});

const link = document.createElement("a");

link.href = URL.createObjectURL(blob);
link.download = "Database_Backup.txt";

link.click();

}

function exportCSV(){

const csv =
`Claim ID,Patient,Hospital,Status
CL031,Rahul Patil,City Care Hospital,Approved
CL030,Sachin More,Metro Hospital,Approved
CL029,Rutuja Patil,Hope Hospital,Approved`;

const blob = new Blob([csv], {type:"text/csv"});

const link = document.createElement("a");

link.href = URL.createObjectURL(blob);
link.download = "Claims_Database.csv";

link.click();

}