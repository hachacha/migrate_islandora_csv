as of now - 8/11/2020

these are the main fields 
```
<mods:title>
<mods:subject>
<mods:publisher>
<mods:dateCreated>
<mods:dateModified>
<mods:dateIssued>
<mods:extent>
<mods:identifier type= "local">
<mods:physicalLocation>
<mods:language>
<mods:accessCondition type="">
accessCondition_link	
<mods:identifier type="doi">
subtitle
description
filename
type
viewingDirection
behavior
```

publisher / author / creator can be used i'll just modify the config file.

dateissued should be iso8601


the following fields are necessary for the migration configuration and iiif manifest generation and some explanation of what they should be.

type

paged_content
image

^ not totally sure what this should be.

every rights/copyright link needs to have the url that corresponds
we need to have a viewingDirection set for each item (I'm not sure how often this will be something other than left-to-right) here are the options

	left-to-right
	right-to-left
	top-to-bottom
	bottom-to-top

here are the options for the rights 
	In Copyright
	In Copyright - EU Orphan Work
	In Copyright - Educational Use Permitted
	In Copyright - Non-commercial Use Permitted
	In Copyright - Rights-Holder(s)
	No Copyright - Contractual Restrictions
	No Copyright - Non-Commercial Use Only
	No Copyright - Other Known Legal Restrictions
	No Copyright - United States
	Copyright Not Evaluated
	Copyright Undetermined
	No Known Copyright
these are the links
	http://rightsstatements.org/vocab/InC/1.0/
	http://rightsstatements.org/vocab/InC-OW-EU/1.0/
	http://rightsstatements.org/vocab/InC-EDU/1.0/
	http://rightsstatements.org/vocab/InC-NC/1.0/
	http://rightsstatements.org/vocab/InC-RUU/1.0/or Unidentifiable
	http://rightsstatements.org/vocab/NoC-CR/1.0/
	http://rightsstatements.org/vocab/NoC-NC/1.0/
	http://rightsstatements.org/vocab/NoC-OKLR/1.0/Restrictions
	http://rightsstatements.org/vocab/NoC-US/1.0/
	http://rightsstatements.org/vocab/CNE/1.0/
	http://rightsstatements.org/vocab/UND/1.0/
	http://rightsstatements.org/vocab/NKC/1.0/
and the links should be from rights org


