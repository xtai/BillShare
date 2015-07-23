var inputs = {
  "datetime": null,
  "userAID": 0,
  "currencyID": 0,
  "amount": null,
  "name": null,
  "category": "for",
  "userBID": 2,
  "note": null
}
var rent = {
  "recordID": 0,
  "datetime": "2015-05-17T18:00:00.000Z",
  "userAID": 0,
  "currencyID": 0,
  "amount": 1365,
  "name": "rent",
  "category": "for",
  "userBID": 2,
  "note": "Rent of First Month, May, 2015"
}
var clean = {
  "datetime": null,
  "userAID": 0,
  "currencyID": 0,
  "amount": null,
  "name": null,
  "category": "for",
  "userBID": 2,
  "note": null
}
var now = new Date();
var rate = 6.2;
var owe;
// Change to numeric keyboard on iOS
$("#amount").on("touchstart", function() {
  $(this).attr("type", "number");
});
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
  $("#collapse-input-groups").collapse("toggle");
  $('#collapse-input-groups').on('shown.bs.collapse', function() {
    $("#show-hidden-buttons").text("Hide");
  });
  $('#collapse-input-groups').on('hidden.bs.collapse', function() {
    $("#show-hidden-buttons").text("Add");
  });
}
var showInputs = function() {
  $("#collapse-input-groups").collapse("show");
  $('#collapse-input-groups').on('shown.bs.collapse', function() {
    $("#show-hidden-buttons").text("Hide");
  });
}
var hideInputs = function() {
  $("#collapse-input-groups").collapse("hide");
  $('#collapse-input-groups').on('hidden.bs.collapse', function() {
    $("#show-hidden-buttons").text("Add");
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
var allRecords;
var allYearsMonths = new Array();
var monthText = new Array(13)
monthText[0] = null;
monthText[1] = "January";
monthText[2] = "February";
monthText[3] = "March";
monthText[4] = "April";
monthText[5] = "May";
monthText[6] = "June";
monthText[7] = "July";
monthText[8] = "August";
monthText[9] = "September";
monthText[10] = "October";
monthText[11] = "November";
monthText[12] = "December";
var initialRecordView = function() {
  $.getJSON("data/record.json", function(data) {
    allRecords = data;
    saveYearMonth();
    showAllMonth();
    addAllRecords();
    calculateAll();
  });
}
var checkInArray = function(array, x) {
  for (var i in array) {
    if (array[i] == x) {
      return true;
    }
  }
  return false;
}
var saveYearMonth = function() {
  for (var i in allRecords) {
    dt = new Date(allRecords[i].datetime);
    var m = 0;
    if (dt.getMonth() < 9) {
      m = "0" + (dt.getMonth() + 1).toString();
    } else {
      m = (dt.getMonth() + 1).toString();
    }
    dtym = parseFloat(dt.getFullYear().toString() + "." + m);
    allRecords[i]["ymID"] = dt.getFullYear().toString() + m;
    if (allYearsMonths.length == 0) {
      allYearsMonths.push(dtym);
    } else {
      if (!checkInArray(allYearsMonths, dtym)) {
        allYearsMonths.push(dtym);
      }
    }
  }
  allYearsMonths.sort();
}
var calculateAll = function() {}
var showAllMonth = function() {
  var ymHTML = new Array();
  for (var i in allYearsMonths) {
    var b = allYearsMonths[i].toString().split(".");
    var ymID = b[0] + b[1];
    var ymColor = "default";
    var ymName = monthText[parseInt(b[1])] + ", " + parseInt(b[0]);
    if (now.getMonth() == (parseInt(b[1]) - 1) && now.getFullYear() == b[0]) {
      ymColor = "info";
    }
    ymHTML.push("<div class=\"month panel panel-" + ymColor + "\">" + "<div class=\"panel-heading\" onclick=\"$('#collapse-" + ymID + "').collapse('toggle')\">" + "<h3 class=\"panel-title\">" + ymName + "</h3></div>" + "<div id=\"collapse-" + ymID + "\" class=\"panel-collapse collapse in\">" + "<div class=\"table-responsive\"><table class=\"table table-hover\">" + "<thead><tr><th></th><th></th><th class=\"text-right\">Zheng</th>" + "<th class=\"text-right\">Xiaoyu</th><th></th></tr></thead>" + "<tbody id=\"record-" + ymID + "\"></tbody></table></div></div>" + "<div class=\"panel-footer\"><p class=\"text-right\" id=\"summary-" + ymID + "\"></p>" + "</div></div>");
  }
  for (var i in ymHTML) {
    $("#records").prepend(ymHTML[i]);
  }
}
var monthlyAmount = new Array(allYearsMonths.length);
var addAllRecords = function() {
  var totalAmount = new Array(2);
  totalAmount[0] = 0;
  totalAmount[1] = 0;
  var getUesrsName = function(id) {
    switch (id) {
      case 0:
        return "Zheng";
      case 1:
        return "Xiaoyu";
      case 2:
        return "house";
      default:
        return;
    }
  }
  var currentName = function(id) {
    switch (id) {
      case 0:
        return "$";
      case 1:
        return "¥";
      default:
        return;
    }
  }
  var uesrsAmount = function(r) {
    var result = new Array(2);
    var amo = parseFloat(r.amount);
    if (r.currencyID == 1) {
      amo = parseFloat(r.amount / rate);
    }
    if (r.category == "to") {
      result[r.userAID] = parseFloat(-amo);
      result[r.userBID] = 0;
    } else if (r.category == "for" && r.userBID == "2") {
      var b;
      if (r.userAID == 0) {
        b = 1
      } else {
        b = 0
      };
      result[r.userAID] = 0;
      result[b] = parseFloat(amo / 2);
    } else {
      result[r.userAID] = 0;
      result[r.userBID] = parseFloat(amo);
    }
    return result;
  }
  var getRecordsDate = function(d) {
    var dt = new Date(d);
    var mm = addZero(dt.getMonth() + 1);
    var dd = addZero(dt.getDate());
    return mm + "/" + dd + "/" + dt.getFullYear().toString();
  }
  var cl = function(cid, num) {
    if (cid == 1) {
      num *= rate;
    }
    if (num == 0) {
      return "";
    } else if (num > 0) {
      return currentName(cid) + num.toFixed(2);
    } else {
      return "-" + currentName(cid) + Math.abs(num).toFixed(2);
    }
  }
  var singleHTML = function(r) {
    var amo = new Array(2);
    var nt = "";
    amo[0] = uesrsAmount(r)[0];
    amo[1] = uesrsAmount(r)[1];
    amo[0] = cl(r.currencyID, amo[0]);
    amo[1] = cl(r.currencyID, amo[1]);
    if (r.note != null) {
      nt = " class=\"note\" data-container=\"body\" data-toggle=\"popover\"" + " data-placement=\"top\" data-trigger=\"hover\" data-content=\"" + r.note + "\"";
    }
    return "<tr><td>" + getRecordsDate(r.datetime) + "</td>" + "<td><b>" + getUesrsName(r.userAID) + "</b> paid <b><abbr" + nt + ">" + currentName(r.currencyID) + r.amount.toFixed(2) + "</abbr></b> " + r.name + " " + r.category + " <b>" + getUesrsName(r.userBID) + "</b></td>" + "<td class=\"text-right\">" + amo[0] + "</td>" + "<td class=\"text-right\">" + amo[1] + "</td>" + "<td class=\"text-center\"><a class=\"btn btn-default btn-xs\" data-toggle=\"modal\" data-target=\"#edit-record-modal\" data-recordid=\"" + r.recordID + "\">&nbsp;<span class=\"glyphicon glyphicon-edit\" aria-hidden=\"true\"></span>&nbsp;</a></td></tr>";
  }
  var getIndexOfArray = function(x, array) {
    for (var it in array) {
      if (x == array[it]) {
        return it;
      }
    }
    return -1;
  }
  var monthlyHTML = function(name, i) {
    var amo = new Array(2);
    amo[0] = cl(0, monthlyAmount[i][0]);
    amo[1] = cl(0, monthlyAmount[i][1]);
    return "<tr><th></th><td class=\"text-right\"><b>Total</b></td>" + "<td class=\"text-right\" id=\"a-" + name + "\">" + amo[0] + "</td>" + "<td class=\"text-right\" id=\"b_" + name + "\">" + amo[1] + "</td>" + "<td></td></tr>";
  }
  var summaryHTML = function(name, i) {
    var owe_acc = 0;
    for (var it in monthlyAmount) {
      if (allYearsMonths[it] <= allYearsMonths[i]) {
        owe_acc += (monthlyAmount[it][1] - monthlyAmount[it][0]);
      }
    }
    return updateOweText(owe_acc, name);
  }
  for (var i in allYearsMonths) {
    monthlyAmount[i] = new Array(2);
    monthlyAmount[i][0] = 0;
    monthlyAmount[i][1] = 0;
  }
  for (var i in allRecords) {
    var ym = parseFloat(allRecords[i].ymID.slice(0, 4) + "." + allRecords[i].ymID.slice(4, 6));
    var index = parseInt(getIndexOfArray(ym, allYearsMonths));
    if (index != -1) {
      monthlyAmount[index][0] += uesrsAmount(allRecords[i])[0];
      monthlyAmount[index][1] += uesrsAmount(allRecords[i])[1];
    }
    totalAmount[0] += uesrsAmount(allRecords[i])[0];
    totalAmount[1] += uesrsAmount(allRecords[i])[1];
  }
  for (var i in allRecords) {
    $("#record-" + allRecords[i].ymID).prepend(singleHTML(allRecords[i]));
  }
  for (var i in allYearsMonths) {
    var b = allYearsMonths[i].toString().split(".");
    var name = b[0] + b[1];
    var ymName = monthText[parseInt(b[1])] + ", " + parseInt(b[0]);
    $("#record-" + name).append(monthlyHTML(name, i));
    $("#summary-" + name).html(summaryHTML(ymName, i));
  }
  owe = totalAmount[1] - totalAmount[0];
  o = updateOwe(owe);
  $(".note").popover();
}
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
var updateInputs = function(data) {
  setUserA(data.userAID);
  setUserB(data.userBID);
  setCurrency(data.currencyID);
  setAmount(data.amount);
  setName(data.name);
  setCategory(data.category);
  showInputs();
}
var addRecord = function() {
  updateInputs(clean);
}
$(document).ready(function() {
  if ($(window).width() < 992) {
    $("#collapse-input-groups").collapse();
    $("#collapse-input-groups").collapse("hide");
  }
  updateInputs(inputs);
  initialRecordView();
  $("#datetimepicker").datetimepicker();
});
// Show Inputs when screen width > 991px
$(window).resize(function() {
  if ($(window).width() < 992) {
    //$("#collapse-input-groups").collapse("hide");
  } else if ($(window).width() > 991) {
    $("#collapse-input-groups").collapse("show");
  }
});