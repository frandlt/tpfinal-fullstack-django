var today = new Date();
var date = today.getDate() + '/' + (today.getMonth() + 1) + '/' + today.getFullYear();

let i = 1;

document.addEventListener("DOMContentLoaded", function(){
    document.getElementById('today').innerHTML = date;
})

document.addEventListener("DOMContentLoaded", function(){
    var tbody = document.getElementById("tbl").tBodies[0];
    console.log(tbody);
    var trs = tbody.getElementsByTagName('tr');
    console.log(trs);
    for (tr of trs){
        tr.querySelector(".num").innerHTML = i;
        tr.querySelector("select").name = String("asist-"+i);
        tr.querySelector(".id-turno").name = String("id-"+i);
        //tr.querySelector(".submit").name = String("submit-"+i);
        i++;
    };
    
})

