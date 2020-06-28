from orden import Orden
from computadora import Computadora
from monitor import Monitor
from teclado import Teclado
from raton import Raton

teclado_hp = Teclado("HP", "USB")
raton_hp = Raton("HP", "USB")
monitor_hp = Monitor("HP", "15 pulgadas")
pc_hp = Computadora("HP", monitor_hp, teclado_hp, raton_hp)

teclado_acer = Teclado("ACER", "Bluetooth")
raton_acer = Raton("ACER", "Bluetooth")
monitor_acer = Monitor("ACER", "27 pulgadas")
pc_acer = Computadora("ACER", monitor_acer, teclado_acer, raton_acer)

teclado_lenovo = Teclado("Lenovo", "USB")
raton_lenovo = Raton("Lenovo", "USB")
monitor_lenovo = Monitor("Lenovo", "47 pulgadas")
pc_lenovo = Computadora("Lenovo", monitor_lenovo, teclado_lenovo, raton_lenovo)

pc_armada = Computadora("Armada", monitor_hp, teclado_acer, raton_lenovo)

computadoras1 = [pc_hp, pc_acer]
orden1 = Orden(computadoras1)
orden1.agregarComputadora(pc_lenovo)
print(orden1)

computadoras2 = [pc_lenovo, pc_armada, pc_acer]
orden2 = Orden(computadoras2)
print(orden2)