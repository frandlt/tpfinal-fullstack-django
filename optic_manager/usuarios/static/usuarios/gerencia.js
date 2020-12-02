$(document).ready(function() {
  $("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
  });  

  $('ul.reporte a').click(function(){
    if(!$(this).hasClass("active")){
        $(".active").removeClass("active");                        
        $(this).addClass("active");

    }else{
        return false;//this prevents flicker
    }
  })
});


document.addEventListener("DOMContentLoaded", function(event) {
    console.log("DOM fully loaded and parsed");
    selection();
  });

function seleccionaCustom() {
  document.getElementById("inputPeriod").value = "custom";
  
  var [start, end] = getCustomDates();
  
  let string = start.toLocaleString().concat(" - ",end.toLocaleString());

  //document.getElementById("resultado").innerHTML = string;
}

function selection() {
  var valor_opcion = document.getElementById("inputPeriod").value;
  
  console.log("valor_opcion = " + valor_opcion);
  
  if(valor_opcion == "this-week")
  {
    var [start, end] = getWeekDates();
    console.log("DONE");
  }
  else if(valor_opcion == "past-week")
  {
    var [start, end] = getPastWeekDates();
    console.log("DONE");
  } else if(valor_opcion == "this-month")
  {
    var [start, end] = getThisMonthDates();
    console.log("DONE");
  } else if(valor_opcion == "past-month")
  {
    var [start, end] = getPastMonthDates();
    console.log("DONE");
  } else if(valor_opcion == "this-year")
  {
    var [start, end] = getThisYearDates();
    console.log("DONE");
  } else if(valor_opcion == "past-year")
  {
    var [start, end] = getPastYearDates();
    console.log("DONE");
  }   else if (valor_opcion == "custom"){
    return;
  }
 
  //let string = start.toLocaleString().concat(" - ",end.toLocaleString());

  //document.getElementById("resultado").innerHTML = string;
  
  //
  var start_to_input, end_to_input;
  
  start_to_input = start.toISOString();
  start_to_input = start_to_input.slice(0,10);
  console.log(start_to_input);
  
  document.getElementById("inputStartDate").value = start_to_input;
  
  end_to_input = end.toISOString();
  end_to_input = end_to_input.slice(0,10);
  console.log(end_to_input);
  
  document.getElementById("inputEndDate").value = end_to_input;
  
}



function getWeekDates() {

  let now = new Date();
  let dayOfWeek = now.getDay(); //0-6
  let numDay = now.getDate();

  let start = new Date(now); //copy
  start.setDate(numDay - dayOfWeek);
  start.setHours(0, 0, 0, 0);


  let end = new Date(now); //copy
  end.setDate(numDay + (6 - dayOfWeek));
  end.setHours(0, 0, 0, 0);

  return [start, end];
}

function getPastWeekDates() {

  let now = new Date();
  let dayOfWeek = now.getDay(); //0-6
  let numDay = now.getDate();

  let start = new Date(now); //copy
  start.setDate(numDay - dayOfWeek - 7);
  start.setHours(0, 0, 0, 0);


  let end = new Date(now); //copy
  end.setDate(numDay + (-1 - dayOfWeek));
  end.setHours(0, 0, 0, 0);

  return [start, end];
}

function getThisMonthDates() {

  let now = new Date();
  //let dayOfWeek = now.setDay(1); //0-6
  //let numMonth = new.getMonth();
  let numDay = 1;

  let start = new Date(now); //copy
  start.setDate(numDay);
  start.setHours(0, 0, 0, 0);


  let end = new Date(now); //copy
  end.setMonth(start.getMonth() + 1);
  end.setDate(0);
  end.setHours(0, 0, 0, 0);

  return [start, end];
}

function getPastMonthDates() {

  let now = new Date();
  //let dayOfWeek = now.setDay(1); //0-6
  let numMonth = now.getMonth();
  let numDay = 1;

  let start = new Date(now); //copy
  start.setDate(numDay);
  start.setMonth(numMonth - 1);
  start.setHours(0, 0, 0, 0);


  let end = new Date(now); //copy
  end.setMonth(numMonth);
  end.setDate(0);
  end.setHours(0, 0, 0, 0);

  return [start, end];
}

function getCustomDates() {

  var inputStart = document.getElementById("inputStartDate").value;
  console.log(inputStart);
  
  let start = new Date(); //copy
  start.setYear(inputStart.slice(0,4));
  start.setMonth(parseInt(inputStart.slice(5,7),10) - 1);
  start.setDate(inputStart.slice(8,10));
  start.setHours(0, 0, 0, 0);
  console.log(start);

  var inputEnd = document.getElementById("inputEndDate").value;
  console.log(inputEnd);
  
  let end = new Date(); //copy
  end.setYear(inputEnd.slice(0,4));
  end.setMonth(parseInt(inputEnd.slice(5,7),10) - 1);
  end.setDate(inputEnd.slice(8,10));
  end.setHours(0, 0, 0, 0);
  console.log(end);

  return [start, end];
}

function getThisYearDates() {

  let now = new Date();
  //let dayOfWeek = now.setDay(1); //0-6
  //let numMonth = new.getMonth();
  let numMonth = 0;
  let numDay = 1;

  let start = new Date(now); //copy
  start.setDate(numDay);
  start.setMonth(numMonth);
  start.setHours(0, 0, 0, 0);


  let end = new Date(now); //copy
  end.setMonth(start.getMonth() + 12);
  end.setDate(0);
  end.setHours(0, 0, 0, 0);

  return [start, end];
}

function getPastYearDates() {

  let now = new Date();
  //let dayOfWeek = now.setDay(1); //0-6
  //let numMonth = new.getMonth();
  let numYear = now.getFullYear();
  let numMonth = 0;
  let numDay = 1;

  let start = new Date(now); //copy
  start.setDate(numDay);
  start.setMonth(numMonth);
  start.setYear(numYear - 1);
  start.setHours(0, 0, 0, 0);


  let end = new Date(now); //copy
  end.setMonth(start.getMonth() + 12);
  end.setDate(0);
  end.setFullYear(start.getFullYear());
  end.setHours(0, 0, 0, 0);

  return [start, end];
}
