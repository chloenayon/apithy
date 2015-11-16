########################
#   helper functions   #
########################

def format_event(a):
    #returns html string
    str = '''
<h3>%s</h3>
<p>
<i>url</i>: %s <br>
<i>description</i>: %s <br>
<i>start time</i>: %s <br>
<i>end time</i>: %s 
</p>
'''
    return str%(a['title'],a['url'],a['description'],a['start_time'],a['stop_time'])
