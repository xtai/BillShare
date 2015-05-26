var currencyID = 0;
var userAID = 0;
var userBID = 1;
var preposition = "for";
var record = {
  "RecordID": 0,
  "Datetime": "2015-05-17T18:00:00.000Z",
  "UserAID": 0,
  "CurrencyID": 0,
  "Amount": 307.45344,
  "Name": "Rent",
  "Category": "for",
  "UserBID": 1,
  "Note": "Rent of First Month, May, 2015"
}

var toggleUserA = function(){
  switch(userAID){
    case 0: setUserA(1); setUserB(0); break;
    case 1: setUserA(0); setUserB(1); break;
    default: break;
  }
}

var toggleCurrency = function(){
  switch(currencyID){
    case 0: setCurrency(1); break;
    case 1: setCurrency(0); break;
    default: break;
  }
}

var togglePrepos = function(){
  if (preposition == "for") {
    preposition = "to";
    if(userAID == 0){
      setUserB(1);  
    }else if(userAID == 1){
      setUserB(0);
    }
    $("#UserB").attr("disabled", true);
  }else if (preposition == "to") {
    preposition = "for";
    $("#UserB").removeAttr("disabled");
  }
  $("#preposition").text(preposition);
}

var toggleUserB = function(){
  if (userAID == 0 && preposition == "for") {
    switch(userBID){
      case 1: setUserB(2); break;
      case 2: setUserB(1); break;
      default: break;
    }
  }else if(userAID == 1 && preposition == "for"){
    switch(userBID){
      case 0: setUserB(2); break;
      case 2: setUserB(0); break;
      default: break;
    }
  }else if (userAID == 0 && preposition == "to") {
    setUserB(1);
  }else if(userAID == 1 && preposition == "to"){
    setUserB(0);
  }
}

var setUserA = function(id){
  switch(id){
    case 0: userAID = 0; $("#UserA").text("Zheng"); break;
    case 1: userAID = 1; $("#UserA").text("Xiaoyu"); break;
    default: break;
  }
}

var setUserB = function(id){
  switch(id){
    case 0: userBID = 0; $("#UserB").text("Zheng"); break;
    case 1: userBID = 1; $("#UserB").text("Xiaoyu"); break;
    case 2: userBID = 2; $("#UserB").text("house"); break;
    default: break;
  }
}

var setCurrency = function(id){
  switch(id){
    case 0: currencyID = 0; $("#currency").text("$"); break;
    case 1: currencyID = 1; $("#currency").text("¥"); break;
    default: break;
  }
}