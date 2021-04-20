	if (message.Content.StartsWith(Prefix + "parabot"))
	{
		Console.WriteLine("[Seg:Joke] Parabot Triggered.");
		await message.Channel.SendMessageAsync("**Parabot by Goose {Sasha}**");
		var nouns = File.ReadAllLines(@"C:\Workspace\Programming\c#\lumite_cache\parabot\nouns.csv");
		string[] computersCan = {"will never", "will always fail to", "can't", "can't ever", "won't ever"};
		string[] whatWillComputers = {"enjoy a", "feel", "know a", "like a", "have a"};
		var random = new Random();
		var parable = "computers";
		var start = random.Next(0, computersCan.Length - 1);
		parable += " ";
		parable += computersCan[start];
		parable += " ";
		var task = random.Next(0, whatWillComputers.Length - 1);
		parable += whatWillComputers[task];
		var noun = random.Next(0, nouns.Length - 1);
        	if (nouns[noun][0] in {"a", "e", "i", "o", "u"} && parable[parable.Length - 1] == "a")
		{
			parable += "n";
		}
		parable += " ";
		parable += nouns[noun];
		await message.Channel.SendMessageAsync(parable);
		
		Console.WriteLine("[Seg:Joke] C# Code to implement Parabot 1.1 into a discord bot.");
	}
