
document.getElementById("boton-select").addEventListener("click", function(){
    document.getElementById("form-diag").style.display = "block";
    document.getElementById("form-select-turno").style.display = "none";
    var radios = document.getElementById("form1").getElementsByClassName("radio");
    var checked_radio = ""
    console.log(radios)
    for (radio of radios){
        if (radio.checked){
            checked_radio = radio;
    }}
    var id_turno = checked_radio.value;
    var x = document.getElementById(`label-${id_turno}`).innerHTML
    document.getElementById("datos_paciente").innerHTML = x;
    document.getElementById("id_turno").value = id_turno;
})

document.getElementById("boton-cambiar").addEventListener("click", function(){
    document.getElementById("form-diag").style.display = "none";
    document.getElementById("form-select-turno").style.display = "block";
})