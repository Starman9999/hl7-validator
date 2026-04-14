# Set format of MSH segment
msh_format = {
    'MSH-1_Field Separator': "|",
    'MSH-2_Encoding Characters': "",
    'MSH-3_Sending Application': "",
    'MSH-4_Sending Facility': "",
    'MSH-5_Receiving Application': "",
    'MSH-6_Receiving Facility': "",
    'MSH-7_Date/Time Of Message': "",
    'MSH-8_Security': "",
    'MSH-9_Message Type': "",
    'MSH-10_Message Control ID': "",
    'MSH-11_Processing ID': "",
    'MSH-12_Version ID': "",
    'MSH-13_Sequence Number': "",
    'MSH-14_Continuation Pointer': "",
    'MSH-15_Accept Acknowledgment Type': "",
    'MSH-16_Application Acknowledgment Type': "",
    'MSH-17_Country Code': "",
    'MSH-18_Character Set': "",
    'MSH-19_Principal Language Of Message': "",
    'MSH-20_Alternate Character Set Handling Scheme': "",
    'MSH-21_Message Profile Identifier': "",
}
msh_format_2 = [ 'MSH-1_Field Separator',
    'MSH-2_Encoding Characters',
    'MSH-3_Sending Application',
    'MSH-4_Sending Facility',
    'MSH-5_Receiving Application',
    'MSH-6_Receiving Facility',
    'MSH-7_Date/Time Of Message',
    'MSH-8_Security',
    'MSH-9_Message Type',
    'MSH-10_Message Control ID',
    'MSH-11_Processing ID',
    'MSH-12_Version ID',
    'MSH-13_Sequence Number',
    'MSH-14_Continuation Pointer',
    'MSH-15_Accept Acknowledgment Type',
    'MSH-16_Application Acknowledgment Type',
    'MSH-17_Country Code',
    'MSH-18_Character Set',
    'MSH-19_Principal Language Of Message',
    'MSH-20_Alternate Character Set Handling Scheme',
    'MSH-21_Message Profile Identifier',]
   
# Sample MSH data
sample_msh = "MSH|^~&|SendingApp|SendingFacility|ReceivingApp|ReceivingFacility|20241109120000||ADT^A01|123456|P|2.3"

# Split the sample MSH segment into component parts, based on the HL7 delimiter (in this case the 'pipe' character)


#values
split_msh = sample_msh.split('|')


# Zip the MSH format 
#message_object = zip(msh_format, msh_tuple)
#print(list(message_object))

message_dict = dict(zip(msh_format_2, split_msh))
print(message_dict)