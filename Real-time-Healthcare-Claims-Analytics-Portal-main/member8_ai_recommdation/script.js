function quickAsk(text){
document.getElementById("userInput").value=text;
sendMessage();
}

function getAIResponse(question){

question=question.toLowerCase();

if(question.includes("claims")){
return "📊 Total Claims: 12,450 | Approved: 10,850 | Rejected: 1,600. Claim processing performance is excellent.";
}

if(question.includes("approved")){
return "✅ Approval Rate: 87%. Average approval time is 2.8 days.";
}

if(question.includes("rejected")){
return "❌ Rejection Rate: 13%. Major reasons include Missing Documents, Invalid Codes and Eligibility Issues.";
}

if(question.includes("fraud")){
return "⚠️ AI Alert: 12 suspicious claims detected. Duplicate billing patterns found in provider submissions.";
}

if(question.includes("cost")){
return "💰 Estimated Savings: ₹4.5 Lakhs. Recommendation: Reduce duplicate claims and automate verification.";
}

if(question.includes("provider")){
return "🏥 Top Provider: Apollo Hospital. Approval Rate: 94%. Average settlement time: 2 days.";
}

if(question.includes("trend")){
return "📈 Monthly Trend: Claims increased by 18% compared to last month. Approval rate improved by 5%.";
}

return "🤖 AI Recommendation: Healthcare claim performance is stable. Focus on reducing rejection rates and monitoring fraud risks.";
}

function sendMessage(){

let input=document.getElementById("userInput");

let text=input.value.trim();

if(text==="") return;

let chat=document.getElementById("chatBox");

chat.innerHTML+=`
<div class="user-message">
<span>${text}</span>
</div>
`;

let response=getAIResponse(text);

chat.innerHTML+=`
<div class="bot-message">
<div class="bot-icon">🤖</div>
<div class="message">${response}</div>
</div>
`;

input.value="";

chat.scrollTop=chat.scrollHeight;

}

document.getElementById("userInput")
.addEventListener("keypress",function(e){

if(e.key==="Enter"){
sendMessage();
}

});