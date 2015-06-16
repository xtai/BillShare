/*
 * Input
 *   // the input component
 * Properties: 
 * - UserIDList.data
 * - UserIDList.uidl
 * Methods:
 * - UserIDList.toggleUserA()
 * - UserIDList.toggleUserB()
 */
var Input = function(data, uidl) {
  if (typeof(data) == 'undefined') {
    this.data = {
      "datetime": null,
      "userAID": 0,
      "currencyID": 0,
      "amount": null,
      "name": null,
      "category": "for",
      "userBID": 2,
      "note": null
    };
  } else {
    this.data = data;
  }
  this.uidl = uidl;
  this.toggleUserA = function() {
    if (category == "for") {
      uidl.nextID(this.data.userAID, true);
    } else {
      uidl.nextID(this.data.userAID, false);
    }
  }
}