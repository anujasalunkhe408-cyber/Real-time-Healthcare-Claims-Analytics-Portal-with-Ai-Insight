/*=====================================================
                DASHBOARD VARIABLES
======================================================*/

const totalEmails = document.getElementById("totalEmails");

const fraudAlerts = document.getElementById("fraudAlerts");

const systemAlerts = document.getElementById("systemAlerts");

const adminNotifications = document.getElementById("adminNotifications");

const pendingReminders = document.getElementById("pendingReminders");

const followupAlerts = document.getElementById("followupAlerts");


/*=====================================================
                COUNTER ANIMATION
======================================================*/

function animateCounter(element, target){

    if(!element) return;

    let count = 0;

    const increment = Math.max(1, Math.ceil(target / 100));

    const timer = setInterval(function(){

        count += increment;

        if(count >= target){

            count = target;

            clearInterval(timer);

        }

        element.innerText = count;

    },20);

}


/*=====================================================
            INITIAL DASHBOARD VALUES
======================================================*/

function loadDashboardCards(){

    animateCounter(totalEmails,1000);

    animateCounter(fraudAlerts,251);

    animateCounter(systemAlerts,5);

    animateCounter(adminNotifications,251);

    animateCounter(pendingReminders,325);

    animateCounter(followupAlerts,87);

}


/*=====================================================
                SMOOTH SCROLL
======================================================*/

document.querySelectorAll(".sidebar a").forEach(link=>{

    link.addEventListener("click",function(e){

        const target=this.getAttribute("href");

        if(target && target.startsWith("#")){

            e.preventDefault();

            const section=document.querySelector(target);

            if(section){

                section.scrollIntoView({

                    behavior:"smooth",

                    block:"start"

                });

            }

        }

    });

});


/*=====================================================
            ACTIVE SIDEBAR MENU
======================================================*/

const menuLinks=document.querySelectorAll(".sidebar a");

menuLinks.forEach(link=>{

    link.addEventListener("click",function(){

        menuLinks.forEach(item=>{

            item.classList.remove("active");

        });

        this.classList.add("active");

    });

});


/*=====================================================
                PAGE LOADED
======================================================*/

window.addEventListener("load",function(){

    loadDashboardCards();

});
/*=====================================================
            EMAIL NOTIFICATION DATA
======================================================*/

function loadEmailNotifications(){

    const approvalClaim=document.getElementById("approvalClaim");
    const approvalPatient=document.getElementById("approvalPatient");

    const rejectionClaim=document.getElementById("rejectionClaim");
    const rejectionPatient=document.getElementById("rejectionPatient");

    const statusClaim=document.getElementById("statusClaim");
    const statusPatient=document.getElementById("statusPatient");

    if(approvalClaim){

        approvalClaim.innerText="C1001";
        approvalPatient.innerText="Rahul Sharma";

    }

    if(rejectionClaim){

        rejectionClaim.innerText="C1008";
        rejectionPatient.innerText="Amit Kumar";

    }

    if(statusClaim){

        statusClaim.innerText="C1025";
        statusPatient.innerText="Priya Patel";

    }

}


/*=====================================================
                FRAUD ALERT POPUP
======================================================*/

const alertModal=document.getElementById("alertModal");

const viewAlertBtn=document.getElementById("viewAlertBtn");

const closeModal=document.getElementById("closeModal");

const reviewClaim=document.getElementById("reviewClaim");


if(viewAlertBtn){

    viewAlertBtn.addEventListener("click",function(){

        alertModal.style.display="flex";

    });

}


if(closeModal){

    closeModal.addEventListener("click",function(){

        alertModal.style.display="none";

    });

}


if(reviewClaim){

    reviewClaim.addEventListener("click",function(){

        alert("Administrator has started reviewing the selected claim.");

        alertModal.style.display="none";

    });

}


/*=====================================================
        CLOSE POPUP WHEN CLICKING OUTSIDE
======================================================*/

window.addEventListener("click",function(e){

    if(e.target===alertModal){

        alertModal.style.display="none";

    }

});


/*=====================================================
        FRAUD ALERT DATA
======================================================*/

function loadFraudAlert(){

    const claimId=document.getElementById("claimId");

    const patientId=document.getElementById("patientId");

    const hospitalId=document.getElementById("hospitalId");

    const riskScore=document.getElementById("riskScore");


    if(claimId){

        claimId.innerText="C1052";

    }

    if(patientId){

        patientId.innerText="P214";

    }

    if(hospitalId){

        hospitalId.innerText="H007";

    }

    if(riskScore){

        riskScore.innerText="96%";

    }


    /* Popup */

    const popupClaim=document.getElementById("popupClaimId");

    const popupPatient=document.getElementById("popupPatientId");

    const popupHospital=document.getElementById("popupHospitalId");


    if(popupClaim){

        popupClaim.innerText="C1052";

    }

    if(popupPatient){

        popupPatient.innerText="P214";

    }

    if(popupHospital){

        popupHospital.innerText="H007";

    }

}


/*=====================================================
            INITIALIZE PART 2
======================================================*/

window.addEventListener("load",function(){

    loadEmailNotifications();

    loadFraudAlert();

});
/*=====================================================
            SYSTEM ALERTS
======================================================*/

function loadSystemAlerts(){

    const databaseStatus=document.getElementById("databaseStatus");

    const aiStatus=document.getElementById("aiStatus");

    const emailStatus=document.getElementById("emailStatus");

    if(databaseStatus){

        databaseStatus.innerText="Database Connected Successfully";

    }

    if(aiStatus){

        aiStatus.innerText="Fraud Detection Model Running";

    }

    if(emailStatus){

        emailStatus.innerText="Email Notification Service Active";

    }

}


/*=====================================================
        ADMINISTRATOR NOTIFICATION
======================================================*/

function loadAdministratorNotification(){

    const notificationClaim=document.getElementById("notificationClaim");

    const notificationStatus=document.getElementById("notificationStatus");

    const notificationTime=document.getElementById("notificationTime");

    if(notificationClaim){

        notificationClaim.innerText="C1052";

    }

    if(notificationStatus){

        notificationStatus.innerText="Unread";

    }

    if(notificationTime){

        notificationTime.innerText=new Date().toLocaleTimeString([],{

            hour:"2-digit",

            minute:"2-digit"

        });

    }

}


/*=====================================================
        REVIEW NOTIFICATION BUTTON
======================================================*/

const reviewNotificationBtn=document.getElementById("reviewNotificationBtn");

if(reviewNotificationBtn){

    reviewNotificationBtn.addEventListener("click",function(){

        const notificationStatus=document.getElementById("notificationStatus");

        if(notificationStatus){

            notificationStatus.innerText="Read";

            notificationStatus.style.color="#10b981";

            notificationStatus.style.fontWeight="700";

        }

        alert("Administrator has reviewed this notification.");

    });

}


/*=====================================================
        SYSTEM STATUS REFRESH
======================================================*/

function refreshSystemStatus(){

    const statuses=document.querySelectorAll(".status");

    statuses.forEach(function(status){

        status.style.opacity="0.7";

        setTimeout(function(){

            status.style.opacity="1";

        },300);

    });

}


/*=====================================================
            AUTO REFRESH
======================================================*/

setInterval(function(){

    refreshSystemStatus();

},5000);


/*=====================================================
            INITIALIZE PART 3
======================================================*/

window.addEventListener("load",function(){

    loadSystemAlerts();

    loadAdministratorNotification();

});
/*=====================================================
            REMINDER SYSTEM
======================================================*/

function loadReminderSystem(){

    /* Pending Claim */

    const pendingClaim=document.getElementById("pendingClaim");

    const pendingPatient=document.getElementById("pendingPatient");


    if(pendingClaim){

        pendingClaim.innerText="C1021";

    }

    if(pendingPatient){

        pendingPatient.innerText="Rahul Sharma";

    }


    /* Deadline Reminder */

    const deadlineClaim=document.getElementById("deadlineClaim");

    const deadlineDate=document.getElementById("deadlineDate");


    if(deadlineClaim){

        deadlineClaim.innerText="C1045";

    }

    if(deadlineDate){

        deadlineDate.innerText="30-06-2026";

    }


    /* Follow-up Alert */

    const followupClaim=document.getElementById("followupClaim");

    const followupPatient=document.getElementById("followupPatient");


    if(followupClaim){

        followupClaim.innerText="C1078";

    }

    if(followupPatient){

        followupPatient.innerText="Amit Kumar";

    }

}


/*=====================================================
        REMINDER CARD HOVER EFFECT
======================================================*/

const reminderCards=document.querySelectorAll(".reminder-card");

reminderCards.forEach(function(card){

    card.addEventListener("mouseenter",function(){

        card.style.transform="translateY(-10px)";

    });

    card.addEventListener("mouseleave",function(){

        card.style.transform="translateY(0px)";

    });

});


/*=====================================================
        REMINDER COUNTER UPDATE
======================================================*/

function updateReminderCount(){

    if(pendingReminders){

        pendingReminders.innerText="325";

    }

    if(followupAlerts){

        followupAlerts.innerText="87";

    }

}


/*=====================================================
        AUTO REFRESH REMINDERS
======================================================*/

function refreshReminderSection(){

    const reminderStatus=document.querySelectorAll(

        ".pending-status,.deadline-status,.followup-status"

    );

    reminderStatus.forEach(function(item){

        item.style.opacity="0.5";

        setTimeout(function(){

            item.style.opacity="1";

        },300);

    });

}


setInterval(function(){

    refreshReminderSection();

},6000);


/*=====================================================
        REMINDER NOTIFICATION
======================================================*/

function reminderPopup(){

    console.log("Reminder System Active");

}


/*=====================================================
            INITIALIZE PART 4
======================================================*/

window.addEventListener("load",function(){

    loadReminderSystem();

    updateReminderCount();

    reminderPopup();

});
/*=====================================================
                ALERT HISTORY
======================================================*/

function loadAlertHistory(){

    const historyTable=document.getElementById("historyTable");

    if(!historyTable){

        return;

    }

    historyTable.innerHTML="";

    const historyData=[

        {

            historyId:"H001",

            claimId:"C1052",

            patientId:"P214",

            hospitalId:"H007",

            priority:"HIGH",

            status:"Unread",

            date:"28-06-2026",

            time:"10:45 AM"

        },

        {

            historyId:"H002",

            claimId:"C1045",

            patientId:"P305",

            hospitalId:"H003",

            priority:"MEDIUM",

            status:"Read",

            date:"28-06-2026",

            time:"11:20 AM"

        },

        {

            historyId:"H003",

            claimId:"C1078",

            patientId:"P188",

            hospitalId:"H015",

            priority:"LOW",

            status:"Read",

            date:"28-06-2026",

            time:"12:10 PM"

        }

    ];


    historyData.forEach(function(item){

        const row=document.createElement("tr");

        row.innerHTML=`

            <td>${item.historyId}</td>

            <td>${item.claimId}</td>

            <td>${item.patientId}</td>

            <td>${item.hospitalId}</td>

            <td>

                <span class="badge ${item.priority.toLowerCase()}">

                    ${item.priority}

                </span>

            </td>

            <td>

                <span class="badge ${item.status.toLowerCase()}">

                    ${item.status}

                </span>

            </td>

            <td>${item.date}</td>

            <td>${item.time}</td>

        `;

        historyTable.appendChild(row);

    });

}


/*=====================================================
            TABLE ROW HOVER
======================================================*/

function enableHistoryHover(){

    const rows=document.querySelectorAll("#historyTable tr");

    rows.forEach(function(row){

        row.addEventListener("mouseenter",function(){

            row.style.background="#eff6ff";

        });

        row.addEventListener("mouseleave",function(){

            row.style.background="white";

        });

    });

}


/*=====================================================
            REFRESH HISTORY
======================================================*/

function refreshHistory(){

    loadAlertHistory();

    enableHistoryHover();

}


/*=====================================================
        AUTO REFRESH HISTORY
======================================================*/

setInterval(function(){

    refreshHistory();

},10000);


/*=====================================================
        INITIALIZE PART 5
======================================================*/

window.addEventListener("load",function(){

    loadAlertHistory();

    enableHistoryHover();

});
/*=====================================================
            DASHBOARD INITIALIZATION
======================================================*/

function initializeDashboard(){

    console.log("========================================");
    console.log("Notifications & Alerts Dashboard");
    console.log("System Initialized Successfully");
    console.log("========================================");

    loadDashboardCards();

    loadEmailNotifications();

    loadFraudAlert();

    loadSystemAlerts();

    loadAdministratorNotification();

    loadReminderSystem();

    updateReminderCount();

    loadAlertHistory();

    enableHistoryHover();

}


/*=====================================================
            LIVE DATE & TIME
======================================================*/

function updateDateTime(){

    const admin=document.querySelector(".admin span");

    if(admin){

        const now=new Date();

        admin.innerText=

        "Administrator | "+

        now.toLocaleDateString()+" | "+

        now.toLocaleTimeString();

    }

}

setInterval(updateDateTime,1000);


/*=====================================================
            BUTTON ANIMATIONS
======================================================*/

const buttons=document.querySelectorAll("button");

buttons.forEach(function(btn){

    btn.addEventListener("mouseenter",function(){

        btn.style.transform="scale(1.05)";

    });

    btn.addEventListener("mouseleave",function(){

        btn.style.transform="scale(1)";

    });

});


/*=====================================================
            CARD ANIMATION
======================================================*/

const cards=document.querySelectorAll(

".card,.email-card,.alert-card,.system-card,.notification-card,.reminder-card"

);

cards.forEach(function(card){

    card.addEventListener("mouseenter",function(){

        card.style.transition=".3s";

    });

});


/*=====================================================
            PAGE LOADED
======================================================*/

document.addEventListener("DOMContentLoaded",function(){

    initializeDashboard();

    updateDateTime();

});


/*=====================================================
            PROJECT INFORMATION
======================================================*/

console.log(

"%cNotifications & Alerts Dashboard",

"color:#2563eb;font-size:18px;font-weight:bold;"

);

console.log(

"%cReal-Time Healthcare Claims Analytics Portal",

"color:#10b981;font-size:14px;"

);

console.log(

"%cFrontend Loaded Successfully",

"color:#7c3aed;font-size:14px;"

);

/*=====================================================
            REMINDER STATUS TABLE
======================================================*/

function loadReminderStatus(){

    const table = document.getElementById("reminderStatusTable");

    if(!table){

        return;

    }

    table.innerHTML = "";

    const reminderStatusData = [

        {

            statusId:"RS001",

            claimId:"C1005",

            type:"Pending Reminder",

            status:"Sent",

            date:"28-06-2026",

            time:"10:15 AM"

        },

        {

            statusId:"RS002",

            claimId:"C1012",

            type:"Deadline Reminder",

            status:"Sent",

            date:"28-06-2026",

            time:"11:40 AM"

        },

        {

            statusId:"RS003",

            claimId:"C1035",

            type:"Follow-up Alert",

            status:"Pending",

            date:"28-06-2026",

            time:"12:20 PM"

        },

        {

            statusId:"RS004",

            claimId:"C1048",

            type:"Pending Reminder",

            status:"Failed",

            date:"28-06-2026",

            time:"01:10 PM"

        }

    ];


    reminderStatusData.forEach(function(item){

        let badgeClass = "";

        if(item.status === "Sent"){

            badgeClass = "status-sent";

        }

        else if(item.status === "Pending"){

            badgeClass = "status-pending";

        }

        else{

            badgeClass = "status-failed";

        }

        const row = document.createElement("tr");

        row.innerHTML = `

            <td>${item.statusId}</td>

            <td>${item.claimId}</td>

            <td>${item.type}</td>

            <td>

                <span class="${badgeClass}">

                    ${item.status}

                </span>

            </td>

            <td>${item.date}</td>

            <td>${item.time}</td>

        `;

        table.appendChild(row);

    });

}


/*=====================================================
        AUTO REFRESH REMINDER STATUS
======================================================*/

function refreshReminderStatus(){

    loadReminderStatus();

}

setInterval(function(){

    refreshReminderStatus();

},8000);


/*=====================================================
        INITIALIZE REMINDER STATUS
======================================================*/

window.addEventListener("load",function(){

    loadReminderStatus();

});


databaseBtn.addEventListener("click", function(){

    window.open("../data/claims.pdf");

});


const emailServiceBtn =
document.getElementById("emailServiceBtn");

emailServiceBtn.addEventListener("click", function(){

    window.open(
        "https://mail.google.com/",
        "_blank"
    );

});