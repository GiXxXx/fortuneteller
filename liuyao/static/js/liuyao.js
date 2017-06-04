//render paipan page
$(document).ready(function(){
    $.ajax({
        method: "GET",
        url: $('#paipan_form').attr('url')
    })
    .done(function(data) {
        console.log(data);
        var $coinSelect = $('<select class="w3-select w3-border"></select>');
        data.yaoSet.forEach(function(element) {
            var option = '<option value=' + element.yao + '>' + element.name + '(' + element.coin + ')</option>';
            $coinSelect.append(option);
        }, this); 

        var count = 0;
        var yao_name = ['liuyao', 'wuyao', 'siyao', 'sanyao', 'eryao', 'chuyao'];
        data.nameSet.forEach(function(element) {
            $coinSelect.attr('name', yao_name[count]);
            var $select_div = $('<div style="margin-top:10px"></div>');
            var $row = $('<tr></tr>');
            var $labelCell = $('<td></td>');
            var $selectCell = $('<td></td>');
            var select_label = '<span>' + element.label + '(第 ' + element.time + ' 次摇币)：</span>';
            $selectCell.append($coinSelect[0].outerHTML);
            $labelCell.append(select_label);
            $row.append($labelCell[0].outerHTML);
            $row.append($selectCell[0].outerHTML);
            $('#liuyao_yaobi_section').append($row);
            count++;
        });
    });
});

$('#liuyao_paipan_button').click(function() {
    console.log($(this).attr('url'))
    $.ajax({
            method: "POST",
            url: $(this).attr('url'),
            data: {
                'date': $('#date').value,
                'gender': $('#gender').value,
                'matter': $('#matter').value,
                'chuyao': $('#chuyao').value,
                'eryao': $('#eryao').value,
                'sanyao': $('#sanyao').value,
                'siyao': $('#siyao').value,
                'wuyao': $('#wuyao').value,
                'liuyao': $('#liuyao').value,
            }
        })
        .done(function(data) {
            console.log(data);
        });

});
//          <tr>
//              <td>性别： {{bengua.gender}}</td>
//                <td>月支：{{bengua.yuezhi}}</td>
//              <td>日支：{{bengua.rizhi}}</td>
//              <td>事项：{{bengua.matter}}</td>
//                <td></td>
//              <td></td>
//            </tr>
//            <tr>
//              <td></td>
//              <td></td>
//              <td></td>
//                <td>{{bengua.gong}}宫：{{bengua.gua}}</td>
//              <td></td>
//              <td>{{biangua.gong}}宫：{{biangua.gua}}</td>
//            </tr>
//            <tr>
//              <td>六神</td>
//              <td>伏神</td>
//              <td>本</td>
//                <td>卦</td>
//              <td>变</td>
//              <td>卦</td>
//            </tr>
//
//              {% for yao_detail in detail %}
//                  <tr>
//                      <td>{{yao_detail.liushen}}</td>
//                      <td>{{yao_detail.fushen}}</td>
//                      <td>{{yao_detail.yao}}</td>
//                        <td>{{yao_detail.yao_xiang}}</td>
//                      <td>{{yao_detail.bian_yao}}</td>
//                      <td>{{yao_detail.bian_yao_xiang}}</td>
//                 </tr>
//              {% endfor %}

var i = 11234;
console.log(i)
//
//$.ajax({
//  method: "GET",
//  url: "http://192.168.1.201/liuyao/panpan",
//})
//  .done(function(data) {
//    console.log(data);
//  });