JS
function calendar(moon){    
    var day = new Date().getDate()
    var dayWeek=moon.phase[day].dayWeek
    var html = "<div>" +
    "<b>" + moon.nameDay[dayWeek]+ "</b>" +
    "<div>" + day + " <b>" + moon.monthName + "</b> " +
    moon.year + "</div>" +
    "<div shadow>" + moon.phase[day].svg + "</div>" +
    "<div>" + moon.phase[day].phaseName + " " +
    "" + ((moon.phase[day].isPhaseLimit )? ""  :   Math.round(moon.phase[day].lighting) + "%") +
    "</div>" +
    "</div>"
    document.getElementById("phase_calendar").innerHTML = html
}   
var configMoon = {
    lang  		:'en', 
    month 		:new Date().getMonth() + 1,
    year  		:new Date().getFullYear(),
    size		:150, 
    lightColor	:"rgb(255,255,210)", 
    shadeColor	:"black", 
    texturize	:false, 
}
load_moon_phases(configMoon, calendar)