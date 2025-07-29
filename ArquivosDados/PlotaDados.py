import matplotlib.pyplot as plt
import numpy as np

def plot_all_sensor_data_styled(filepath):
    try:
        data = np.loadtxt(filepath, delimiter=',', skiprows=1, dtype=float)

        if data.size == 0:
            print(f"O ficheiro '{filepath}' está vazio ou não contém dados válidos.")
            return

        data_50_samples = data[:50]

        if data_50_samples.size == 0:
            print(f"O ficheiro '{filepath}' não contém dados suficientes para 50 amostras.")
            return

        numero_amostra = data_50_samples[:, 0].astype(float)
        accel_x = data_50_samples[:, 1].astype(float)
        accel_y = data_50_samples[:, 2].astype(float)
        accel_z = data_50_samples[:, 3].astype(float)
        giro_x = data_50_samples[:, 4].astype(float)
        giro_y = data_50_samples[:, 5].astype(float)
        giro_z = data_50_samples[:, 6].astype(float)

        tempo_s = numero_amostra * 0.1

        column_names = ['Aceleração X', 'Aceleração Y', 'Aceleração Z',
                        'Giroscópio X', 'Giroscópio Y', 'Giroscópio Z']
        data_arrays = [accel_x, accel_y, accel_z, giro_x, giro_y, giro_z]

        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
        linestyles = ['-', '--', ':', '-.', '-', '--']
        markers = ['o', 's', '^', 'd', 'x', 'P']
        marker_interval = max(1, len(numero_amostra) // 10)

        fig, axes = plt.subplots(3, 2, figsize=(14, 12))
        fig.suptitle('Dados do Sensor MPU6050 ao Longo do Tempo', fontsize=18, fontweight='bold')

        for i, (name, arr) in enumerate(zip(column_names, data_arrays)):
            row = i // 2
            col_in_row = i % 2

            axes[row, col_in_row].plot(
                tempo_s, arr,
                color=colors[i],
                linestyle=linestyles[i],
                marker=markers[i],
                markevery=marker_interval,
                linewidth=1.5
            )
            axes[row, col_in_row].set_title(name, fontsize=14, fontweight='bold')
            axes[row, col_in_row].set_xlabel('Tempo (s)', fontsize=12)
            axes[row, col_in_row].set_ylabel('Valor do Sensor', fontsize=12)
            axes[row, col_in_row].grid(True, linestyle='--', alpha=0.7)
            axes[row, col_in_row].tick_params(axis='both', which='major', labelsize=10)

        plt.tight_layout(rect=[0, 0.04, 1, 0.96])
        plt.show()

    except FileNotFoundError:
        print(f"Erro: O ficheiro '{filepath}' não foi encontrado.")
    except IndexError:
        print(f"Erro: O ficheiro '{filepath}' não tem o número esperado de colunas (7). Verifique o formato dos dados.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    # Caminho corrigido para o ficheiro, incluindo a subpasta 'ArquivosDados'
    data_file = 'ArquivosDados/mpu6050_data.txt'
    plot_all_sensor_data_styled(data_file)
