from addressing import addresser

from protobuf import user_pb2
from protobuf import product_pb2

class SupplyState(object):
    def __init__(self, context, timeout=2):
        self._context = context
        self._timeout = timeout

    def get_user(self, public_key):
        """Gets the agent associated with the public_key
        Args:
            public_key (str): The public key of the agent
        Returns:
            agent_pb2.Agent: Agent with the provided public_key
        """
        address = addresser.get_user_address(public_key)
        state_entries = self._context.get_state(
            addresses=[address], timeout=self._timeout)
        if state_entries:
            container = user_pb2.UserContainer()
            container.ParseFromString(state_entries[0].data)
            for user in container.entries:
                if user.public_key == public_key:
                    return user

    def set_user(self, public_key, username, role, timestamp):
        user_address = addresser.get_user_address(public_key)

        user = user_pb2.User(
            public_key = public_key,
            username=username,
            role=role
            )
        container = user_pb2.UserContainer()
        state_entries = self._context.get_state(
            addresses=[user_address], timeout=self._timeout)
        if state_entries:
            container.ParseFromString(state_entries[0].data)

        container.entries.extend([user])
        data = container.SerializeToString()

        updated_state = {}
        updated_state[user_address] = data
        self._context.set_state(updated_state, timeout=self._timeout)


    def get_product(self, id):
        address = addresser.get_product_address(id)
        state_entries = self._context.get_state(
            addresses=[address], timeout=self._timeout)
        if state_entries:
            container = product_pb2.ProductContainer()
            container.ParseFromString(state_entries[0].data)
            for product in container.entries:
                if product.id == id:
                    return product

        return None
    def drug_import(self,
        timestamp,
        id,
        name
    ):
        product_address = addresser.get_product_address(id)

        product = product_pb2.Product(
            id=id,
            name=name
        )
        container = product_pb2.ProductContainer()
        state_entries = self._context.get_state(
            addresses=[product_address], timeout=self._timeout)
        if state_entries:
            container.ParseFromString(state_entries[0].data)

        container.entries.extend([product])
        data = container.SerializeToString()

        updated_state = {}
        updated_state[product_address] = data
        self._context.set_state(updated_state, timeout=self._timeout)



    def update_status(self,
        timestamp,
        id,
        quantity,
        price
    ):
        product_address = addresser.get_product_address(id)
        status = product_pb2.Product.Status(
            timestamp = timestamp,
            quantity = quantity,
            price = price
        )
        container = product_pb2.ProductContainer()
        state_entries = self._context.get_state(
            addresses=[product_address], timeout=self._timeout)
        if state_entries:
            container.ParseFromString(state_entries[0].data)
            for product in container.entries:
                if product.id == id:
                    product.statuss.extend([status])

        data = container.SerializeToString()
        updated_state = {}
        updated_state[product_address] = data
        self._context.set_state(updated_state, timeout=self._timeout)

    def update_location(self,
        timestamp,
        id,
        longitude,
        latitude
    ):
        product_address = addresser.get_product_address(id)
        location = product_pb2.Product.Location(
            timestamp = timestamp,
            longitude = longitude,
            latitude = latitude
        )
        container = product_pb2.ProductContainer()
        state_entries = self._context.get_state(
            addresses=[product_address], timeout=self._timeout)
        if state_entries:
            container.ParseFromString(state_entries[0].data)
            for product in container.entries:
                if product.id == id:
                    product.locations.extend([location])

        data = container.SerializeToString()
        updated_state = {}
        updated_state[product_address] = data
        self._context.set_state(updated_state, timeout=self._timeout)
