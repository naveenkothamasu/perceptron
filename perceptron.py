

For each class c
	wc = 0;
	For N Iierations
		For each training example (xi, yi)
			zi = argmax wx * f(xi)
			if zi != yi:
				wzi = wzi - f(xi);
				wyi = wyi + f(xi);
		
