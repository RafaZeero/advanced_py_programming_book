from random import uniform

from main import Particle, ParticleSimulator


def benchmark():
    particles = [
        Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0))
        for _ in range(10)
    ]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)


# if __name__ == "__main__":
#     benchmark()
