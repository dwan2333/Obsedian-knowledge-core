
Configure conda-forge as default package
	1, ==conda config --add channels conda-forge==
			It adds a new source for downloading packages called **conda-forge** and puts it at the **top** of your priority list.
	2, ==conda config --set channels_priority strict==
			"If a package is in the top channel, take it from there. Do NOT look at lower channels, even if they have a newer version."


Creating 
	1,==conda create -y -n pydata-book python=3.10==
		-y = yes
		-n = name
		so it basically create a new environment 

Activation
	1,==conda activate pydata-book==
		activate the environment 

Install and update 
	1,==conda install package name== 
	2,==conda update package name==