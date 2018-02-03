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

<h1>Illugi</h1>
<h1>Þversumma</h1>
<h2>kennitala : {{kt}}, = þversumma = {{summa}} </h2>
%end
</body>
</html>
