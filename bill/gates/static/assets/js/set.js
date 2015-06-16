var setCategory = function(id) {
  switch (id) {
    case "for":
      inputs.category = "for";
      $("#UserB").removeAttr("disabled");
      $("#category").text(inputs.category);
      break;
    case "to":
      inputs.category = "to";
      if (inputs.userAID == 0) {
        setUserB(1);
      } else if (inputs.userAID == 1) {
        setUserB(0);
      }
      $("#UserB").attr("disabled", true);
      $("#category").text(inputs.category);
      break;
    default:
      break;
  }
}
var setUserA = function(id) {
  switch (id) {
    case 0:
      inputs.userAID = 0;
      rent.userAID = 0;
      $("#UserA").text("Zheng");
      break;
    case 1:
      inputs.userAID = 1;
      rent.userAID = 1;
      $("#UserA").text("Xiaoyu");
      break;
    default:
      break;
  }
}
var setUserB = function(id) {
  switch (id) {
    case 0:
      inputs.userBID = 0;
      $("#UserB").text("Zheng");
      break;
    case 1:
      inputs.userBID = 1;
      $("#UserB").text("Xiaoyu");
      break;
    case 2:
      inputs.userBID = 2;
      $("#UserB").text("house");
      break;
    default:
      break;
  }
}
var setCurrency = function(id) {
  switch (id) {
    case 0:
      inputs.currencyID = 0;
      $("#currency").text("$");
      break;
    case 1:
      inputs.currencyID = 1;
      $("#currency").text("¥");
      break;
    default:
      break;
  }
}
var setAmount = function(x) {
  if (x == null) {
    $("#amount").attr("value", "");
  } else {
    $("#amount").attr("value", x.toFixed(2));
  }
}
var setName = function(x) {
  if (x == null) {
    $("#things").attr("value", "");
  } else {
    $("#things").attr("value", x);
  }
}