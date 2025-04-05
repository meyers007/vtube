DEFAULT_APP = "vtube"

'''
You can include this in your html pages and refer to these variables:
For example:

	{{ appname }}

'''
import geoapp.analytics as analytics
#---------------------------------------------------------------------------------
def appcontext(request):
    context = {
        "appname": "VTube",
        "weburl" : "https://www.vtube.org/",
        "top_url": "vtube/topbar.html",
        "APP_MENU" : 0,              # Show Application Menu in topbar
        "NO_LOGIN_MENU": 0,          # Show login menu in topbar
        "SSO": 0,                    # Show Signle Sign on
        "DO_NOT_SHOW_LOGIN" : 0,     # DO not allow usernme/passwd -> Just SSO
		"ALLOW_REGISTRATION": 0,     # Allow registering (self registration)
    }    
    analytics.loganalytics(request);
    
    return context
