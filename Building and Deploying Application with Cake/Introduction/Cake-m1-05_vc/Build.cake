var target = Argument<string>("Target");

Task("MyFirstTask")
	.Does(()=>
	{
		Information("Hello, Cake");
	}
);

RunTarget(target)