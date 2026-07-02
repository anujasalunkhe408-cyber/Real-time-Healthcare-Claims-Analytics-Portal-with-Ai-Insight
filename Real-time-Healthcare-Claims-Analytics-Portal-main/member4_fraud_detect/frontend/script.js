/*=========================================================
        AI FRAUD DETECTION DASHBOARD
        SCRIPT.JS (PART 1)
=========================================================*/

document.addEventListener("DOMContentLoaded", function () {

    console.log("Dashboard Loaded Successfully");

    /*=========================================
            DASHBOARD COUNTER ANIMATION
    =========================================*/

    function animateValue(id, start, end, duration, suffix = "") {

        const element = document.getElementById(id);

        if (!element) return;

        let startTimestamp = null;

        const step = (timestamp) => {

            if (!startTimestamp) startTimestamp = timestamp;

            const progress = Math.min((timestamp - startTimestamp) / duration, 1);

            const value = Math.floor(progress * (end - start) + start);

            element.innerHTML = value + suffix;

            if (progress < 1) {

                window.requestAnimationFrame(step);

            }

        };

        window.requestAnimationFrame(step);

    }

    animateValue("totalClaims", 0, 1000, 1500);

    animateValue("fraudClaims", 0, 251, 1500);

    animateValue("riskScore", 0, 89, 1500, "%");



    /*=========================================
                MODEL ACCURACY
    =========================================*/

    const accuracy = document.getElementById("modelAccuracy");

    if (accuracy) {

        accuracy.innerHTML = "98.5%";

    }



    /*=========================================
                SIDEBAR ACTIVE MENU
    =========================================*/

    const menuLinks = document.querySelectorAll(".sidebar a");

    menuLinks.forEach(link => {

        link.addEventListener("click", function () {

            menuLinks.forEach(item => item.classList.remove("active"));

            this.classList.add("active");

        });

    });



    /*=========================================
                SMOOTH SCROLL
    =========================================*/

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {

        anchor.addEventListener("click", function (e) {

            const target = document.querySelector(this.getAttribute("href"));

            if (!target) return;

            e.preventDefault();

            target.scrollIntoView({

                behavior: "smooth"

            });

        });

    });



    /*=========================================
            PAGE LOAD ANIMATION
    =========================================*/

    const sections = document.querySelectorAll(".section");

    sections.forEach((section, index) => {

        section.style.opacity = "0";

        section.style.transform = "translateY(30px)";

        setTimeout(() => {

            section.style.transition = ".7s";

            section.style.opacity = "1";

            section.style.transform = "translateY(0px)";

        }, index * 200);

    });



    console.log("Part 1 Loaded");

});


    /*=========================================================
                    FRAUD ALERT POPUP
    =========================================================*/

    const fraudBtn = document.getElementById("fraudAlertBtn");

    const fraudModal = document.getElementById("fraudModal");

    const cancelBtn = document.getElementById("cancelBtn");

    const okBtn = document.getElementById("okBtn");

    const viewAlertBtn = document.getElementById("viewAlertBtn");

    if(fraudBtn){

        fraudBtn.addEventListener("click",function(e){

            e.preventDefault();

            fraudModal.style.display="flex";

        });

    }

    if(viewAlertBtn){

        viewAlertBtn.addEventListener("click",function(){

            alert(
` FRAUD ALERT

Claim ID      : C0015
Patient ID    : P302
Hospital ID   : H005
Risk Score    : 90%
Status        : HIGH RISK`
            );

        });

    }

    if(cancelBtn){

        cancelBtn.addEventListener("click",function(){

            fraudModal.style.display="none";

        });

    }

    if(okBtn){

        okBtn.addEventListener("click",function(){

            fraudModal.style.display="none";

            document.getElementById("alerts").scrollIntoView({

                behavior:"smooth"

            });

        });

    }

    window.addEventListener("click",function(e){

        if(e.target===fraudModal){

            fraudModal.style.display="none";

        }

    });




    /*=========================================================
                ADMIN NOTIFICATION
    =========================================================*/

    const notificationBtn=document.getElementById("notificationBtn");

    if(notificationBtn){

        notificationBtn.addEventListener("click",function(){

            alert(
`Administrator Notification

High Risk Claim Detected

Claim ID : C0015
Claim ID : C0047
Claim ID : C0091

Please review immediately.`
            );

        });

    }




    /*=========================================================
                DOWNLOAD REPORT
    =========================================================*/

    const downloadBtn=document.getElementById("downloadBtn");

    if(downloadBtn){

        downloadBtn.addEventListener("click",function(){

            const image=document.getElementById("fraudChart");

            if(!image){

                alert("Chart image not found.");

                return;

            }

            const link=document.createElement("a");

            link.href="images/fraud_chart.pdf";

            link.download="Fraud_Report.pdf";

            document.body.appendChild(link);

            link.click();

            document.body.removeChild(link);

        });

    }




    /*=========================================================
                CARD HOVER EFFECT
    =========================================================*/

    const cards=document.querySelectorAll(".card");

    cards.forEach(card=>{

        card.addEventListener("mouseenter",function(){

            this.style.transform="translateY(-12px)";

        });

        card.addEventListener("mouseleave",function(){

            this.style.transform="translateY(0px)";

        });

    });




    /*=========================================================
                BUTTON RIPPLE EFFECT
    =========================================================*/

    const buttons=document.querySelectorAll("button");

    buttons.forEach(button=>{

        button.addEventListener("click",function(){

            this.style.transform="scale(.96)";

            setTimeout(()=>{

                this.style.transform="scale(1)";

            },150);

        });

    });




    /*=========================================================
                CHART ANIMATION
    =========================================================*/

    const chart=document.getElementById("fraudChart");

    if(chart){

        chart.style.opacity="0";

        setTimeout(()=>{

            chart.style.transition=".8s";

            chart.style.opacity="1";

        },700);

    }

    console.log("Part 2 Loaded");


    /*=========================================================
        LOAD AI INSIGHTS JSON
=========================================================*/

fetch("data/ai_insights.json")

.then(response => {

    if (!response.ok) {

        throw new Error("AI Insights file not found.");

    }

    return response.json();

})

.then(data => {

    if(document.getElementById("totalClaims"))
        document.getElementById("totalClaims").innerHTML = data.total_claims;

    if(document.getElementById("fraudClaims"))
        document.getElementById("fraudClaims").innerHTML = data.fraud_claims;

    if(document.getElementById("modelAccuracy"))
        document.getElementById("modelAccuracy").innerHTML = data.model_accuracy + "%";

    if(document.getElementById("riskScore"))
        document.getElementById("riskScore").innerHTML = data.highest_risk + "%";

    if(document.getElementById("aiTotalClaims"))
        document.getElementById("aiTotalClaims").innerHTML = data.total_claims;

    if(document.getElementById("highestClaim"))
        document.getElementById("highestClaim").innerHTML = "₹" + data.highest_claim;

    if(document.getElementById("topHospital"))
        document.getElementById("topHospital").innerHTML = data.top_hospital;

    if(document.getElementById("topDisease"))
        document.getElementById("topDisease").innerHTML = data.top_disease;

})

.catch(error=>{

    console.log(error);

});



/*=========================================================
        LOAD FRAUD ALERT
=========================================================*/

fetch("data/alert.json")

.then(response=>response.json())

.then(data=>{

    if(document.getElementById("claimId"))
        document.getElementById("claimId").innerHTML=data.claim_id;

    if(document.getElementById("patientId"))
        document.getElementById("patientId").innerHTML=data.patient_id;

    if(document.getElementById("hospitalId"))
        document.getElementById("hospitalId").innerHTML=data.hospital_id;

    if(document.getElementById("riskValue"))
        document.getElementById("riskValue").innerHTML=data.risk_score+"%";

    if(document.getElementById("popupClaimId"))
        document.getElementById("popupClaimId").innerHTML=data.claim_id;

    if(document.getElementById("popupPatientId"))
        document.getElementById("popupPatientId").innerHTML=data.patient_id;

    if(document.getElementById("popupHospitalId"))
        document.getElementById("popupHospitalId").innerHTML=data.hospital_id;

    if(document.getElementById("popupRisk"))
        document.getElementById("popupRisk").innerHTML=data.risk_score+"%";

})

.catch(error=>{

    console.log(error);

});



/*=========================================================
        LOAD ADMIN NOTIFICATION
=========================================================*/

fetch("data/admin_notification.json")

.then(response=>response.json())

.then(data=>{

    if(document.getElementById("notificationText")){

        document.getElementById("notificationText").innerHTML=data.message;

    }

})

.catch(error=>{

    console.log(error);

});



/*=========================================================
        LOAD FRAUD LOGS
=========================================================*/

fetch("data/fraud_logs.json")

.then(response=>response.json())

.then(data=>{

    const table=document.getElementById("logTable");

    if(!table) return;

    table.innerHTML="";

    data.forEach(log=>{

        table.innerHTML+=`

        <tr>

            <td>${log.claim_id}</td>

            <td>${log.patient_id}</td>

            <td>${log.hospital_id}</td>

            <td>${log.risk_score}%</td>

            <td>${log.status}</td>

        </tr>

        `;

    });

})

.catch(error=>{

    console.log(error);

});



/*=========================================================
        LIVE DATE & TIME
=========================================================*/

function updateClock(){

    const now=new Date();

    console.log("Dashboard Updated : "+now.toLocaleTimeString());

}

setInterval(updateClock,1000);



/*=========================================================
        DASHBOARD READY
=========================================================*/

console.log("AI Fraud Detection Dashboard Ready");