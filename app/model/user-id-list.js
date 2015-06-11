/*
 * UserIDList
 *   // maintain a user id list
 * Properties: 
 * - UserIDList.userIDList
 * Methods:
 * - UserIDList.addUsersByIDList(array)
 * - UserIDList.addUserByID(uid)
 * - UserIDList.nextID(uid, withHouse)
 */
var UserIDList = function() {
  // maintain a user id list
  this.userIDList = new Array();
  this.addUsersByIDList = function(list) {
    for (var x in list) {
      this.addUserByID(list[x]);
    }
  }
  this.addUserByID = function(uid) {
    this.userIDList.push(parseInt(uid));
  }
  this.nextID = function(uid, withHouse) {
    // find next user in line (for toggling input)
    // uid: number, "current uesr id"
    // withHouse: bollean, "skipping house or not" 
    if (this.userIDList.length <= 0) {
      return -1;
    }
    var next = this.userIDList.indexOf(parseInt(uid));
    if (next == -1) {
      return -1;
    }
    next++;
    if (next >= this.userIDList.length) {
      next = 0;
      if (!withHouse) {
        return this.userIDList[1];
      }
    } else {
      return this.userIDList[next];
    }
  }
}