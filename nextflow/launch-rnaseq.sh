nextflow run nf-core/rnaseq \
	-profile docker,awsbatch \
	-work-dir s3://genomic-nextflow/ \
	--awsqueue genomic-nextflow-queue \
	--awsregion us-east-1 \
	--input s3://genomic-nextflow/sample.csv \
	--outdir s3://genomic-nextflow/output/ \
	--nf_core_pipeline rnaseq \
	--download_method sratools