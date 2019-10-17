import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
logger.setLevel(logging.INFO)


class Machine:
    _req_quantity = 0
    _amount_received = 0
    _req_prod_id = 0

    _amount_remaining = 0
    _quantity_dispatched = 0
    _products_supported = range(1)
    _products_price = [(x+1) * 5 for x in _products_supported]

    def getQuantity(self):
        self._req_quantity = int(input('Enter required Quantity:'))

    def getAmount(self):
        self._amount_received = int(input('Enter Amount:'))

    def processReq(self):
        #initalize _quantity_dispatched and _amount_remaining
        self._quantity_dispatched = self._amount_remaining = 0

        #check if entered valid product
        if self._req_prod_id not in self._products_supported:
            logger.debug('Invalid product id !!')
            return self._quantity_dispatched, self._amount_remaining

        #check if amount is valid
        if self._amount_received <= 0:
            logger.debug('Invalid amount !!')
            return self._quantity_dispatched, self._amount_remaining

        #check if quantity is valid
        if self._req_quantity <= 0:
            logger.debug('Invalid quantity !!')
            self._amount_remaining = self._amount_received
            return self._quantity_dispatched, self._amount_remaining

        #calculate total amount requried or the quantity requested
        total = self._req_quantity * self._products_price[self._req_prod_id]

        #check if amount is sufficient to dispatch
        if total > self._amount_received :
            logger.debug('Insufficient amount !!')
            self._amount_remaining = self._amount_received
            return self._quantity_dispatched, self._amount_remaining
        else :
            logger.debug('!! Success !!')
            self._amount_remaining = self._amount_received - total
            self._quantity_dispatched = self._req_quantity

        #update _quantity_dispatched and _amount_remaining
        return self._quantity_dispatched, self._amount_remaining

if __name__ == '__main__':
    vm = Machine()
    vm.getQuantity()
    vm.getAmount()
    print(vm.processReq())