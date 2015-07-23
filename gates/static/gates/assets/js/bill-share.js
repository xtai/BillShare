g = gravatar("{{ user.email }}", {size: 50, backup: "retro"});
$(".global-avatar").attr("src", g);