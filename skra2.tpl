<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>

<body>
%summa=0
{{kt}}
%for i in kt:
    %summa=summa+int(i)
%end

<h1>Þórður</h1>
<h1>Þversumma</h1>
<h2>kennitala : {{kt}}, 1+6+0+8+0+0+3+6+4+0 = þversumma = {{summa}} </h2>
%end
</body>
</html>
