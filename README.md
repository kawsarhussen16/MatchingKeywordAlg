# Challenge Details
Assume you are designing a performance application to match keywords found in a url. What data structures / technologies would you employ to ensure a speedy (sub 10ns) algorithm that is able to match substrings against the URL?
To help shape your thinking, let's assume that we're dealing with a finite subset of words. This may help bound which algorithms would be most applicable for this problem. 
Please also provide an actual code sample. It's always helpful to see a running example, but obviously doesn't need to be anything "production-ready."

-----

# Challenge FAQs
Q: Are the keywords of interest determined via configuration/external inputs and are we simply seeing if these words show up anywhere in the url?  Could they be domain or in the query string?
A: Yes, the keywords could be anywhere in the url or query string. 

Q: Assuming that the keywords are via configuration, should I expect a few hundred, thousand or large enough amounts such that they could not fit in memory within a single process?  
A: At this point, assume that the keywords would be small enough to fit within a single process.

Q: I understand the idea that a keyword would (in all normal cases) be a substring of the url. In the second sentence, is the word substrings an alias for keywords?
A: Yes, we are using substring as a synonym for keyword, with the additional characteristic that the keyword / substring can potentially be multiple words. For example, a keyword could potentially be "target-this-string" versus being limited to the individual words "target", "this", "string".


