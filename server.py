from http.server import SimpleHTTPRequestHandler
from xmlrpc.server import SimpleXMLRPCRequestHandler, SimpleXMLRPCServer
from robot import francasterController, allbotsController, armController


def register_robot_xmlrpc_methods(server: SimpleXMLRPCServer):
    server.register_function(francasterController.set_motor_position, 'francaster-set_motor_position')
    server.register_function(francasterController.shift_motor_position, 'francaster-shift_motor_position')

    server.register_function(francasterController.walk_n_steps, 'francaster-walk_n_steps')
    server.register_function(francasterController.do_hi, 'francaster-do_hi')
    server.register_function(francasterController.reset_position, 'francaster-reset_position')
    server.register_function(francasterController.set_delay, 'francaster-sleep')
    server.register_function(francasterController.walk_n_steps_with_knee_lift,
                             'francaster-walk_n_steps_with_knee_lift')
    server.register_function(francasterController.do_yes, 'francaster-do_yes')
    server.register_function(francasterController.do_no, 'francaster-do_no')

    server.register_function(allbotsController.reset_position, 'allbots-reset_position')
    server.register_function(allbotsController.set_motor_position, 'allbots-set_motor_position')
    server.register_function(allbotsController.shift_motor_position, 'allbots-shift_motor_position')
    
    server.register_function(armController.plus, 'armController.plus')    
    server.register_function(armController.moins, 'armController.moins')
    server.register_function(armController.tourne, 'armController.tourne')
    server.register_function(armController.position, 'armController.position')
    
    server.register_function(armController.led_on, 'armController.led_on')    
    server.register_function(armController.led_off, 'armController.led_off')
    server.register_function(armController.led_clignote, 'armController.led_clignote')
    server.register_function(armController.bouton, 'armController.excute')




# We define a custom server request handler, capable of both handling GET and XML-RPC requests.
class RequestHandler(SimpleXMLRPCRequestHandler, SimpleHTTPRequestHandler):
    rpc_paths = ('/RobotControlService',)

    def do_GET(self):
        SimpleHTTPRequestHandler.do_GET(self)


if __name__ == "__main__":
    # Create our XML-RPC server.using out custom request handler that is also able to serve web pages over GET.
    port = 8080
    server = SimpleXMLRPCServer(("", port), RequestHandler, allow_none=True)

    # Register standard XML-RPC methods.
    server.register_introspection_functions()

    register_robot_xmlrpc_methods(server)

    # Start to server.
    server.serve_forever()
