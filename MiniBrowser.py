import mechanize
import cookielib

# Browser
br = mechanize.Browser()
# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
# br.set_debug_http(True)
# br.set_debug_redirects(True)
# br.set_debug_response(True)

# User-Agent (this is cheating, OK?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

## Now we have got a Browser


# First set the https and http proxy
# Proxy
# br.set_proxies({"http":"127.0.0.1:8087", "https":"127.0.0.1:8087"})

## Open some site, let's pick the facebook for example.
# r = br.open('https://www.facebook.com')
# br.select_form(nr=0)
# br.form['email'] = 'snaillonely@gmail.com'
# br.form['pass'] = 'Tianshui.86'
# br.submit()
# Write the source to Show the source




## Some useful functions

# Write the html file
def writeHtml(content):
    f = open('temp.html', 'w')
    f.write(content)
    f.close()

