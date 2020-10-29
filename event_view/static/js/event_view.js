// 期間フィルタボタンが押されたときの処理
$('input[name="period_type"]').on("change", function () {
  // ボタンに対応するラベルを取得
  label = $('label[for="' + this.id + '"]');
  // 各イベントの poster を取得
  posters = $('div[class="poster"][name="' + this.value + '"]');
  // ラジオボタンがチェックされていればボタンをactiveにして、ポスターを表示させる
  if ($(this).prop("checked")) {
    label.addClass("active");
    posters.each(function (i, elm) {
      $(elm).parent().show("fast");
    });
  } else {
    label.removeClass("active");
    posters.each(function (i, elm) {
      $(elm).parent().hide("fast");
    });
  }
});
