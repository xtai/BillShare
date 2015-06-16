var all_records;
var year_month = new Array();
var month_text = new Array(13)
month_text[0] = null;
month_text[1] = "January";
month_text[2] = "February";
month_text[3] = "March";
month_text[4] = "April";
month_text[5] = "May";
month_text[6] = "June";
month_text[7] = "July";
month_text[8] = "August";
month_text[9] = "September";
month_text[10] = "October";
month_text[11] = "November";
month_text[12] = "December";
var initialRecordView = function() {
  $.getJSON("/static/data/record.json", function(data) {
    all_records = data;
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
  for (var i in all_records) {
    dt = new Date(all_records[i].datetime);
    var m = 0;
    if (dt.getMonth() < 9) {
      m = "0" + (dt.getMonth() + 1).toString();
    } else {
      m = (dt.getMonth() + 1).toString();
    }
    dt_ym = parseFloat(dt.getFullYear().toString() + "." + m);
    all_records[i]["ym_id"] = dt.getFullYear().toString() + m;
    if (year_month.length == 0) {
      year_month.push(dt_ym);
    } else {
      if (!checkInArray(year_month, dt_ym)) {
        year_month.push(dt_ym);
      }
    }
  }
  year_month.sort();
}
var calculateAll = function() {}
var showAllMonth = function() {
  var ym_html = new Array();
  for (var i in year_month) {
    var b = year_month[i].toString().split(".");
    var ym_id = b[0] + b[1];
    var ym_color = "default";
    var ym_name = month_text[parseInt(b[1])] + ", " + parseInt(b[0]);
    if (now.getMonth() == (parseInt(b[1]) - 1) && now.getFullYear() == b[0]) {
      ym_color = "info";
    }
    ym_html.push("<div class=\"month panel panel-" + ym_color + "\">" + "<div class=\"panel-heading\" onclick=\"$('#collapse_" + ym_id + "').collapse('toggle')\">" + "<h3 class=\"panel-title\">" + ym_name + "</h3></div>" + "<div id=\"collapse_" + ym_id + "\" class=\"panel-collapse collapse in\">" + "<div class=\"table-responsive\"><table class=\"table table-hover\">" + "<thead><tr><th></th><th></th><th class=\"text-right\">Zheng</th>" + "<th class=\"text-right\">Xiaoyu</th><th></th></tr></thead>" + "<tbody id=\"record_" + ym_id + "\"></tbody></table></div></div>" + "<div class=\"panel-footer\"><p class=\"text-right\" id=\"summary_" + ym_id + "\"></p>" + "</div></div>");
  }
  for (var i in ym_html) {
    $("#records").prepend(ym_html[i]);
  }
}
var month_amo = new Array(year_month.length);
var addAllRecords = function() {
  var total_amo = new Array(2);
  total_amo[0] = 0;
  total_amo[1] = 0;
  var usr_name = function(id) {
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
  var cur_name = function(id) {
    switch (id) {
      case 0:
        return "$";
      case 1:
        return "¥";
      default:
        return;
    }
  }
  var usr_amo = function(r) {
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
  var rec_date = function(d) {
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
      return cur_name(cid) + num.toFixed(2);
    } else {
      return "-" + cur_name(cid) + Math.abs(num).toFixed(2);
    }
  }
  var single_html = function(r) {
    var amo = new Array(2);
    var nt = "";
    amo[0] = usr_amo(r)[0];
    amo[1] = usr_amo(r)[1];
    amo[0] = cl(r.currencyID, amo[0]);
    amo[1] = cl(r.currencyID, amo[1]);
    if (r.note != null) {
      nt = " class=\"note\" data-container=\"body\" data-toggle=\"popover\"" + " data-placement=\"top\" data-trigger=\"hover\" data-content=\"" + r.note + "\"";
    }
    return "<tr><td>" + rec_date(r.datetime) + "</td>" + "<td><b>" + usr_name(r.userAID) + "</b> paid <b><abbr" + nt + ">" + cur_name(r.currencyID) + r.amount.toFixed(2) + "</abbr></b> " + r.name + " " + r.category + " <b>" + usr_name(r.userBID) + "</b></td>" + "<td class=\"text-right\">" + amo[0] + "</td>" + "<td class=\"text-right\">" + amo[1] + "</td>" + "<td class=\"text-center\"><a class=\"btn btn-default btn-xs\" data-toggle=\"modal\" data-target=\"#editRecord\" data-recordid=\"" + r.recordID + "\">&nbsp;<span class=\"glyphicon glyphicon-edit\" aria-hidden=\"true\"></span>&nbsp;</a></td></tr>";
  }
  var get_index = function(x, array) {
    for (var it in array) {
      if (x == array[it]) {
        return it;
      }
    }
    return -1;
  }
  var month_html = function(name, i) {
    var amo = new Array(2);
    amo[0] = cl(0, month_amo[i][0]);
    amo[1] = cl(0, month_amo[i][1]);
    return "<tr><th></th><td class=\"text-right\"><b>Total</b></td>" + "<td class=\"text-right\" id=\"a_" + name + "\">" + amo[0] + "</td>" + "<td class=\"text-right\" id=\"b_" + name + "\">" + amo[1] + "</td>" + "<td></td></tr>";
  }
  var summary_html = function(name, i) {
    var owe_acc = 0;
    for (var it in month_amo) {
      if (year_month[it] <= year_month[i]) {
        owe_acc += (month_amo[it][1] - month_amo[it][0]);
      }
    }
    return updateOweText(owe_acc, name);
  }
  for (var i in year_month) {
    month_amo[i] = new Array(2);
    month_amo[i][0] = 0;
    month_amo[i][1] = 0;
  }
  for (var i in all_records) {
    var ym = parseFloat(all_records[i].ym_id.slice(0, 4) + "." + all_records[i].ym_id.slice(4, 6));
    var index = parseInt(get_index(ym, year_month));
    if (index != -1) {
      month_amo[index][0] += usr_amo(all_records[i])[0];
      month_amo[index][1] += usr_amo(all_records[i])[1];
    }
    total_amo[0] += usr_amo(all_records[i])[0];
    total_amo[1] += usr_amo(all_records[i])[1];
  }
  for (var i in all_records) {
    $("#record_" + all_records[i].ym_id).prepend(single_html(all_records[i]));
  }
  for (var i in year_month) {
    var b = year_month[i].toString().split(".");
    var name = b[0] + b[1];
    var ym_name = month_text[parseInt(b[1])] + ", " + parseInt(b[0]);
    $("#record_" + name).append(month_html(name, i));
    $("#summary_" + name).html(summary_html(ym_name, i));
  }
  owe = total_amo[1] - total_amo[0];
  o = updateOwe(owe);
  $(".note").popover();
}