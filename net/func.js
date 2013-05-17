

function GetHeight() {
    var h = screen.height;
    return h;
}

function GetWidth() {
    var w = screen.width;
    return w;
}

function GetAHeight() {
    var h = screen.availHeight;
    return h;
}

function GetAWidth() {
    var w = screen.availWidth;
    return w;
}

function GetColDepth() {
    var c = screen.colorDepth;
    return c;
}

function GetPixelDepth() {
    var p = window.screen.pixelDepth;
    return p;
}

function GetPlugins()
{
  var strPlugins='';
  var numPlugins = navigator.plugins.length;
  for (i = 0; i < numPlugins; i++) 
  {
    plugin = navigator.plugins[i];
    strPlugins=strPlugins+plugin.name+'<br>';
  }
  return strPlugins;
}

function BrowserVersion()
{
  var nVer = navigator.appVersion;
  return nVer;
}

function TimeZonePlusDST()
{
  var now = new Date();
  var later = new Date();
  var tzo = now.getTimezoneOffset()/60 *(-1);
  var d1 = new Date();
  var d2 = new Date();
  d1.setDate(1);
  d1.setMonth(1);
  d2.setDate(1);
  d2.setMonth(7);
  if(parseInt(d1.getTimezoneOffset())==parseInt(d2.getTimezoneOffset())){
   var tzd = 0;
  }else{
   var hemisphere = parseInt(d1.getTimezoneOffset())-parseInt(d2.getTimezoneOffset());
   if((hemisphere>0 && parseInt(d1.getTimezoneOffset())==parseInt(now.getTimezoneOffset())) ||  (hemisphere<0 && parseInt(d2.getTimezoneOffset())==parseInt(now.getTimezoneOffset()))) {
     var tzd = 0;
   }else{
     var tzd = 1;
   }
  }
  return tzo+"."+tzd;
 }


