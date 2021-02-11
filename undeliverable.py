def deademail (row):
    if row['m_Status'] == 'DELIVERED':
        return 'Delivered'
    elif  row['m_Status'] == 'FILTERED':
        return 'Filtered'
    elif row['m_Status'] == 'EXPIRED':
        return 'Expired'
    if row['Group'] == 'Other':    
        if ('invalid') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'        
        elif ('no mx') in str(row['m_LogEntry']).lower():
            return 'No MX'
        elif ('unknown') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif ('mail box') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'        
        elif ('not exist') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'    
        elif ('address rejected') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif ('account locked') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif ('mailbox') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif ('user not known') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'             
        elif ('recipient undeliverable') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif ('recipient') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif ('no such') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif ('could not be found') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif ('not found') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif ('No user') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif ('deleted') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif ('disabled') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif ('permanent') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif ('relay') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif ('route') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif ('unroutable') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif ('verify') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif ('is not') in str(row['m_LogEntry']).lower() and row['m_Status'] == 'BOUNCED':
            return 'Undeliverable email'
        elif ('unable') in str(row['m_LogEntry']).lower() and row['m_Status'] == 'BOUNCED':
            return 'Undeliverable email'
        elif ('quota') in str(row['m_LogEntry']).lower():
            return 'Other Over Quota'    
        elif 'invalid' in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'        
        elif 'no mx' in str(row['m_LogEntry']).lower():
            return 'No MX'
        elif 'unknown' in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'    
        elif 'not exist' in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'    
        elif 'recipient address rejected' in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif 'recipient undeliverable' in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif 'recipientnotfound' in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif 'no such' in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif 'could not be found' in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif 'not found' in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif 'No user' in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif 'deleted' in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif 'disabled' in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif 'permanent' in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif 'relay' in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif 'route' in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif 'unroutable' in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif 'verify' in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'
        elif 'is not' in str(row['m_LogEntry']).lower() and row['m_Status'] == 'BOUNCED':
            return 'Undeliverable email'
        elif 'unable' in str(row['m_LogEntry']).lower() and row['m_Status'] == 'BOUNCED':
            return 'Undeliverable email'
        elif 'quota' in str(row['m_LogEntry']).lower():
            return 'Over Quota'                 
        return 'Other Unknown'
    elif row['Group'] == '1&1':
        if row['m_StatusCode'] == '5.5.0':
            return 'Undeliverable email'        
        else:
            return '1&1 Unknown'
    elif row['Group'] == 'Apple':
        if row['m_StatusCode'] == '4.5.0':
            return 'Over Quota'                  
        elif '5.5.2' in row['m_StatusCode']:
            return 'Over Quota'
        else:
            return 'Apple Unknown'
    elif row['Group'] == 'BT': 
        if '4.5.0' in row['m_StatusCode']:
            return 'Undeliverable email'     
        elif '4.5.1' in row['m_StatusCode']:
            return 'Undeliverable email'     
        else:
            return 'BT Unknown'
    elif row['Group'] == 'Google':                 
        if '4.5.2' in row['m_StatusCode']:
            return 'Over Quota'
        elif '5.0.1' in row['m_StatusCode']:
            return 'Undeliverable email'
        elif '5.5.2' in row['m_StatusCode']:
            return 'Over Quota'       
        else:
            return 'Google Unknown'
    elif row['Group'] == 'GMail':               
        if '4.5.2' in row['m_StatusCode']:
            return 'Over Quota'
        elif '5.0.1' in row['m_StatusCode']:
            return 'Undeliverable email'
        elif '5.5.2' in row['m_StatusCode']:
            return 'Over Quota'       
        else:
            return 'GMail Unknown'
    elif row['Group'] == 'Kcom':        
            return 'Kcom Unknown'
    elif row['Group'] == 'Microsoft':
        if '5.0.1' in row['m_StatusCode']:
            return 'Undeliverable email' 
        else:
            return 'Microsoft Unknown'
    elif row['Group'] == 'Office365':
        if '5.0.1' in row['m_StatusCode']:
            return 'Office365 Undeliverable email'   
        else:
            return 'Office365 Unknown'
    elif row['Group'] == 'Talk Talk':  
        if row['m_StatusCode'] == '5.5.0':
            return 'Undeliverable email'
        else:
            return 'Talk Talk Unknown'
    elif row['Group'] == 'Verizon':  
        if row['m_StatusCode'] == '5.5.4':
            return 'Undeliverable email'    
        elif ('mailbox not found') in str(row['m_LogEntry']).lower():
            return 'Undeliverable email'  
        else:
            return 'Verizon Unknown'
    elif row['Group'] == 'Virgin':
        if row['m_StatusCode'] == '5.5.0':
            return 'Undeliverable email'    
        else:
            return 'Virgin Unknown'
    return 'Unknown'