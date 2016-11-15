//Pause makes counter blink, Resume to remove
(function ($) {
    "use strict";

    /*global window */

    var l4f = {
        init: function () {

            $(".arrow-up").on("click", function () {
                var num = Number($("#id_number_of_players").val());
                if (num < 3) {
                    $("#id_number_of_players").val((num + 1).toString());
                }
            });

            $(".arrow-down").on("click", function () {
                var num = Number($("#id_number_of_players").val());
                if (num > 1) {
                    $("#id_number_of_players").val((num - 1).toString());
                }
            })

            var callhistory = setInterval(function () {
                $.ajax({
                    url: "/l4f/history/",
                    dataType: "json",
                    method: "POST",
                    success: function () {
                        console.log(data);
                    }
                })
            }, 1000);
        }

    };

    l4f.init();
}(window.jQuery));
