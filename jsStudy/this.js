let user = {
  name: "Джон",
  go: function() { console.log(this.name) }
};

(user.go)()
