# vit-en-python-7

"Unicorn" is a term used in the venture capital industry to describe a privately held startup company with a value of over $1 billion (kaggle.com).

Assume that you have the dataset file (unicorns2021.txt) of the startups having the unicorn status in 2021. Each row (line) of this dataset represents information regarding a specific startup.

There are seven (7) different information in each line, each separated by a semicolon character (';'):

    Company: Name of the startup company

    Valuation: Valuation of the company in billion dollars ($ sign appears in the beginning of each record)

    Date joined: The date at which company started working

    Country: Country where the company resides

    City: City of origin for the company.

    Industry: Industry that the company belongs to

    Investors: People who have invested into that company.

How would you find and display the average valuation of the companies that originated from a user-provided city?

Please note that you cannot make any assumptions on the number of lines in the given dataset.

Hint: After splitting the entire line, you can access the city name using line[4] since it is located in the fourth position, considering that Python uses zero-based indexing. Similarly, to retrieve the valuation, you use int(line[1][1:]), which involves converting the second element of the split line to an integer. The notation [1][1:] is used to extract a portion of the string, excluding the first character.

Pseudo code:

Retrieve a city name from the user, then read the related document named 'unicorns2021.txt.' Initialize temporary variables, 'linecounter' and 'valuation,' both set to zero.

Perform a for loop to iterate through all the lines in the document.

Identify lines that contain the specified city name.

Retrieve the valuation values associated with the identified city.

Add each valuation to the cumulative total. Increase 'linecounter' by 1 for each relevant line encountered.

Calculate the average by dividing the total valuation by 'linecounter.'"
