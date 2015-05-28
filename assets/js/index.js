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
var owe;
$(document).ready(function() {
  updateInputs(inputs);
  initialRecordView();
});
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