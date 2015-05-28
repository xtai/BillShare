// Change to numeric keyboard on iOS
$("#amount").on("touchstart", function() {
  $(this).attr("type", "number");
});
$("#amount").on("keydown blur", function() {
  $(this).attr("type", "text");
});
// Show Inputs when screen width > 991px
$(document).ready(function() {
  if ($(window).width() < 992) {
    $("#collapseInputs").collapse();
    $("#collapseInputs").collapse("hide");
  }
});
$(window).resize(function() {
  if ($(window).width() < 992) {
    //$("#collapseInputs").collapse("hide");
  } else if ($(window).width() > 991) {
    $("#collapseInputs").collapse("show");
  }
})
var toggleUserA = function() {
  switch (inputs.userAID) {
    case 0:
      setUserA(1);
      if (inputs.userBID != 2) {
        setUserB(0);
      }
      break;
    case 1:
      setUserA(0);
      if (inputs.userBID != 2) {
        setUserB(1);
      }
      break;
    default:
      break;
  }
}
var toggleCurrency = function() {
  switch (inputs.currencyID) {
    case 0:
      setCurrency(1);
      break;
    case 1:
      setCurrency(0);
      break;
    default:
      break;
  }
}
var toggleCategory = function() {
  if (inputs.category == "for") {
    setCategory("to");
  } else if (inputs.category == "to") {
    setCategory("for");
  }
}
var toggleUserB = function() {
  if (inputs.userAID == 0 && inputs.category == "for") {
    switch (inputs.userBID) {
      case 1:
        setUserB(2);
        break;
      case 2:
        setUserB(1);
        break;
      default:
        break;
    }
  } else if (inputs.userAID == 1 && inputs.category == "for") {
    switch (inputs.userBID) {
      case 0:
        setUserB(2);
        break;
      case 2:
        setUserB(0);
        break;
      default:
        break;
    }
  } else if (inputs.userAID == 0 && inputs.category == "to") {
    setUserB(1);
  } else if (inputs.userAID == 1 && inputs.category == "to") {
    setUserB(0);
  }
}
// Show inputs group on screen width < 768px
var toggleInputs = function() {
  $("#collapseInputs").collapse("toggle");
  $('#collapseInputs').on('shown.bs.collapse', function() {
    $("#showHideButton").text("Hide");
  });
  $('#collapseInputs').on('hidden.bs.collapse', function() {
    $("#showHideButton").text("Add");
  });
}
var showInputs = function() {
  $("#collapseInputs").collapse("show");
  $('#collapseInputs').on('shown.bs.collapse', function() {
    $("#showHideButton").text("Hide");
  });
}
var hideInputs = function() {
  $("#collapseInputs").collapse("hide");
  $('#collapseInputs').on('hidden.bs.collapse', function() {
    $("#showHideButton").text("Add");
  });
}
var updateOweText = function(owe, dt) {
  var t;
  if (owe > 0) {
    t = "<b>Xiaoyu</b> owes <b>Zheng</b> <abbr>$" + Math.abs(owe).toFixed(2) + "</abbr>.";
  } else if (owe < 0) {
    t = "<b>Zheng</b> owes <b>Xiaoyu</b> <abbr>$" + Math.abs(owe).toFixed(2) + "</abbr>.";
  } else {
    t = "we are clear!"
  }
  return "<span class=\"hidden-xs\">As for </span><abbr>" + dt + "</abbr>, " + t;
}
var addZero = function(input) {
  if (input < 9) {
    return "0" + input;
  } else {
    return input;
  }
}
var updateOwe = function(owe) {
  var date = (addZero(now.getMonth() + 1)) + "/" + addZero(now.getDate()) + "/" + now.getFullYear()
  $("#owe-text").html(updateOweText(owe, date));
  var ua;
  var ub;
  if (owe != 0) {
    if (owe > 0) {
      ua = 1;
      ub = 0;
    } else {
      ua = 0;
      ub = 1;
    }
    return o = {
      "datetime": now,
      "userAID": ua,
      "currencyID": 0,
      "amount": Math.abs(owe),
      "name": "back",
      "category": "to",
      "userBID": ub,
      "note": "Paid back on " + now.toString()
    };
  }
  return;
}
$('#loadMore').on('click', function() {
  var $btn = $(this).button('loading');
  //  $btn.button('reset');
})
var allLoaded = function() {
  $('#loadMore').attr("disabled", "true");
  $('#loadMore').text("All records loaded");
}