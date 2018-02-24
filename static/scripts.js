$ ('#orderdate, #shipdate').datepicker();

$ ('#tabs').tabs();

$ ('#customerid').change(function(){
  var custid = $(this).val();
  $.ajax({
    type : 'GET',
    url : '/customer'+'/'+custid,
    dataType: "json",
    cache: false,
    success : function(result){
      $('#custid').val(custid);
      $('#custname').val(result.customername);
      $('#custadd1').val(result.customeradd1);
      $('#custadd2').val(result.customeradd2);
      $('#custcity').val(result.customercity);
      $('#custstate').val(result.customerstate);
      $('#custzip').val(result.customerzip);
      $('#customername').val(result.customername);
    }
  });
});

$ ('#customername').change(function(){
  var custname = $(this).val();
  $.ajax({
    type : 'GET',
    url : '/customer'+'/'+custname,
    dataType: "json",
    cache: false,
    success : function(result){
      $('#custid').val(custid);
      $('#custname').val(result.customername);
      $('#custadd1').val(result.customeradd1);
      $('#custadd2').val(result.customeradd2);
      $('#custcity').val(result.customercity);
      $('#custstate').val(result.customerstate);
      $('#custzip').val(result.customerzip);
      $('#customername').val(result.customername);
    }
  });
});

$ ('#billto').bind("change", function(){
  var custid = $(this).val();
  $.ajax({
    type : 'GET',
    url : '/customer'+'/'+custid,
    dataType: "json",
    cache: false,
    success : function(result){
      $('#billtoname').val(result.customername);
      $('#billtoaddr1').val(result.customeradd1);
      $('#billtoaddr2').val(result.customeradd2);
      $('#billtoaddrcsz').val(result.customercity + ", " + result.customerstate+ "   "+ result.customerzip);
    }
  });
});
