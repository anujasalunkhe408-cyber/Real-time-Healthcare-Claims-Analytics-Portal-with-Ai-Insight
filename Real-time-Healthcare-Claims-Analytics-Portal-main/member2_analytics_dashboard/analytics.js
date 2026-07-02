function show(id){
document.querySelectorAll(".section").forEach(sec=>{
sec.classList.remove("active");
});
document.getElementById(id).classList.add("active");
}

/* FILTER */
function filterTable(){

let s=document.getElementById("search").value.toLowerCase();
let st=document.getElementById("status").value.toLowerCase();
let d=document.getElementById("dept").value.toLowerCase();
let dt=document.getElementById("date").value;

let rows=document.querySelectorAll("#table tr");

for(let i=1;i<rows.length;i++){

let c=rows[i].children;

let ok =
(c[1].innerText.toLowerCase().includes(s) || c[2].innerText.toLowerCase().includes(s)) &&
(st=="" || c[5].innerText.toLowerCase().includes(st)) &&
(d=="" || c[3].innerText.toLowerCase().includes(d)) &&
(dt=="" || c[6].innerText==dt);

rows[i].style.display = ok ? "" : "none";
}
}

function clearFilters(){
document.getElementById("search").value="";
document.getElementById("status").value="";
document.getElementById("dept").value="";
document.getElementById("date").value="";
filterTable();
}


/* PIE */
new Chart(document.getElementById("pieChart"),{
type:"pie",
data:{
labels:["Approved","Pending","Rejected"],
datasets:[{
data:[18,6,6],
backgroundColor:["#22c55e","#f59e0b","#ef4444"]
}]
}
});

/* BAR */
new Chart(document.getElementById("barChart"),{
type:"bar",
data:{
labels:["Cardiology","Neurology","Oncology","Ortho","General"],
datasets:[{
data:[7,5,6,6,6],
backgroundColor:"#2563eb"
}]
}
});

/* LINE */
new Chart(document.getElementById("lineChart"),{
type:"line",
data:{
labels:["Week1","Week2","Week3","Week4"],
datasets:[{
data:[5,8,12,7],
borderColor:"#2563eb",
fill:false
}]
}
});