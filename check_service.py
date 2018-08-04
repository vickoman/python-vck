#!/usr/bin/env python
import subprocess
import shlex
import mandrill

MANDRILL_API_KEY = 'IP1PUpCy1PspPo3gpEpSBw'


def run_command(cmd):
    cmd = shlex.split(cmd)
    return subprocess.check_output(cmd).decode('ascii')

def test_service(service):
        if service == 'chaucer-sandbox-server':
                return run_command('status chaucersandserver')
        elif service == 'portal-service':
                return run_command('status portalservice')
        else:
                return False

def send_mailto_alert(message):
        mandrill_client = mandrill.Mandrill(MANDRILL_API_KEY)
        return mandrill_client.messages.send(message = message)



service_portal = test_service('portal-service')
service_chaucer_sandbox_server = test_service('chaucer-sandbox-server')

if service_portal.split(" ")[1][:-1].split('/')[1] == 'running':
        print "Portal de servicios esta: %s " % service_portal.split(" ")[1][:-1].split('/')[1]
else:
        message = { 'from_email': 'noreply@chaucercloud.com',
          'from_name': 'Portal Services Failure',
          'to': [{
            'email': 'vdiaz@metrodigi.com',
            'name': 'Victor Diaz',
            'type': 'to'
           },{
                'email': 'drivas@metrodigi.com',
                'name': 'David Rivas',
                'type': 'to'
           },{
                'email': 'vicmandlagasca@mgmail.com',
                'name': 'Victor Diaz De La Gasca',
                'type': 'to'
           }],
          'subject': "Portal Services Failure",
          'html': "<p>Portal Services is: <b>%s</b></p> \r\n <p>Please use this command to restart/start the service <i><b>sudo start portalservice</b></i>" % service_portal
        }
        send_mailto_alert(message)
if service_chaucer_sandbox_server.split(" ")[1][:-1].split('/')[1] == 'running':
        print "El Chaucer Sandbox Server esta: %s " % service_chaucer_sandbox_server.split(" ")[1][:-1].split('/')[1]
else:
        """El servidor del chaucer sandbox no esta corriendo"""
        message = { 'from_email': 'noreply@chaucercloud.com',
          'from_name': 'Portal Services Failure',
          'to': [{
            'email': 'vdiaz@metrodigi.com',
            'name': 'Victor Diaz',
            'type': 'to'
           },{
                'email': 'vicmandlagasca@gmail.com',
                'name': 'Victor Diaz De La Gasca',
                'type': 'to'
           }],
          'subject': "Portal Services Failure",
          'html': "<p>Chaucer Sandbox Server is: <b>%s</b></p> \r\n <p>Please use this command to restart/start the service <i><b>sudo start chaucersandserver</b></i>" % service_chaucer_sandbox_server
        }
        send_mailto_alert(message)
